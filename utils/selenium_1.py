import pymongo
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

WINDOWS_HANDLE_DICT = {}
mongo_conf = 'mongodb://192.168.8.200:27017'
instance = pymongo.MongoClient(mongo_conf)
db = instance['selenium']
element = db['WebElement']


class WebElement:
    def __init__(self, id=None, name=None, css=None, text=None, xpath=None):
        self.ID = id
        self.NAME = name
        self.CSS_SELECTOR = css
        self.LINK_TEXT = text
        self.XPATH = xpath


element_exchange = WebElement(**element.find_one({'name': '账号登录'}, {"_id": 0})['element'])
element_username = WebElement(**element.find_one({'name': '用户名'}, {"_id": 0})['element'])
element_password = WebElement(**element.find_one({'name': '密码'}, {"_id": 0})['element'])
element_login = WebElement(**element.find_one({'name': '登录按钮'}, {"_id": 0})['element'])

element_publish = WebElement(**element.find_one({'name': '发布运单'}, {"_id": 0})['element'])
element_order_name = WebElement(**element.find_one({'name': '货物名称'}, {"_id": 0})['element'])
element_cargo = WebElement(**element.find_one({'name': '无烟煤'}, {"_id": 0})['element'])
element_cargo_category = WebElement(**element.find_one({'name': '货物计量'}, {"_id": 0})['element'])
element_order_weight = WebElement(**element.find_one({'name': '货物吨位'}, {"_id": 0})['element'])
element_order_packing = WebElement(**element.find_one({'name': '货物包装'}, {"_id": 0})['element'])
element_vehicle_type_id = WebElement(**element.find_one({'name': '车辆类型'}, {"_id": 0})['element'])
element_vehicle_no_limit = WebElement(**element.find_one({'name': '不限车辆'}, {"_id": 0})['element'])
element_carriage_length_id = WebElement(**element.find_one({'name': '车长类型'}, {"_id": 0})['element'])
element_carriage_length_no_limit = WebElement(**element.find_one({'name': '不限车长'}, {"_id": 0})['element'])
element_despatch_start = WebElement(**element.find_one({'name': '最早到场时间'}, {"_id": 0})['element'])
element_despatch_end = WebElement(**element.find_one({'name': '最晚到场时间'}, {"_id": 0})['element'])
element_receipt_start = WebElement(**element.find_one({'name': '收货时间'}, {"_id": 0})['element'])
element_cargo_money = WebElement(**element.find_one({'name': '整车货值'}, {"_id": 0})['element'])
element_admin_username = WebElement(**element.find_one({'name': '后台登录账号'}, {"_id": 0})['element'])
element_admin_password = WebElement(**element.find_one({'name': '后台登录密码'}, {"_id": 0})['element'])
element_admin_login = WebElement(**element.find_one({'name': '后台登录按钮'}, {"_id": 0})['element'])

element_vehicle_type = WebElement(xpath="//span[contains(.,'车型要求')]")
element_carriage_length = WebElement(xpath="//span[contains(.,'车长要求')]")


class BaseChrome(webdriver.Chrome):
    def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
        super().__init__(executable_path=executable_path,
                         port=port,
                         options=options,
                         service_args=service_args,
                         desired_capabilities=desired_capabilities,
                         service_log_path=service_log_path,
                         chrome_options=chrome_options,
                         keep_alive=keep_alive)

    def find_element_by_selenium(self, element_location):
        for key, value in element_location.__dict__.items():
            if value and key != 'js':
                try:
                    ele = self.find_element(by=eval('By.' + key), value=value)
                    time.sleep(0.1)
                    self.execute_script("arguments[0].scrollIntoView({block: 'center'});", ele)
                    time.sleep(0.1)
                    return ele
                except WebDriverException as e:
                    print(key, value, e)
            elif value and key == 'js':
                return self.execute_script(value)
            else:
                pass

    def open(self, url=None):
        WINDOWS_HANDLE_DICT['last'] = WINDOWS_HANDLE_DICT['current']
        WINDOWS_HANDLE_DICT['current'] = self.current_window_handle
        WINDOWS_HANDLE_DICT[url] = self.current_window_handle
        self.maximize_window()
        self.get(url)

    def open_new_window_tab(self, url):
        js = 'window.open("{url}")'.format(url=url)
        self.execute_script(js)
        for handle in self.window_handles:
            self.switch_to.window(handle)
            if self.current_url == url:
                WINDOWS_HANDLE_DICT[url] = handle
        self.switch_to.window(WINDOWS_HANDLE_DICT[url])


class Functions:

    def open(self, url=None):
        self.get(url)
        self.maximize_window()


class Chrome(BaseChrome, Functions):
    """docstring for Chrome"""

    def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
        BaseChrome.__init__(self, executable_path=executable_path,
                            port=port,
                            options=options,
                            service_args=service_args,
                            desired_capabilities=desired_capabilities,
                            service_log_path=service_log_path,
                            chrome_options=chrome_options,
                            keep_alive=keep_alive)
        Functions.__init__(self)

    def _time_control_set(self, time_str):
        self.switch_to.frame(0)
        time.sleep(0.2)
        self.find_element(By.XPATH, "//td[@onclick='day_Click({time});']".format(time=time_str)).click()
        ele1 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]")
        self.execute_script("arguments[0].focus();", ele1)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]").send_keys('9')
        ele2 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]")
        self.execute_script("arguments[0].focus();", ele2)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]").send_keys('05')
        self.find_element(By.XPATH, '//input[@id="dpOkInput"]').click()
        self.switch_to.parent_frame()
        time.sleep(0.1)

    def change_window_tab(self, url=None):
        self.switch_to.window(WINDOWS_HANDLE_DICT[url])

    def login(self, user_name, password):
        if self.current_url == 'http://sit.zczy-web.zczy.com/modules/mms/system/login.html':
            try:
                self.find_element_by_selenium(element_exchange).click()
                self.find_element_by_selenium(element_username).send_keys(user_name)
                self.find_element_by_selenium(element_password).send_keys(password)
                self.find_element_by_selenium(element_login).click()
                if self.title != '我的智运-个人中心':
                    self.save_screenshot('登陆失败.png')
            except Exception as e:
                print(e)
                self.save_screenshot('1.png')
                self.quit()
        elif self.current_url == 'http://sit.boss-admin.zczy.com/login.html':
            driver.find_element_by_selenium(element_admin_username).send_keys(user_name)
            driver.find_element_by_selenium(element_admin_password).send_keys(password)
            driver.find_element_by_selenium(element_admin_login).click()

    def publish(self):
        self.find_element_by_selenium(element_publish).click()
        self.find_element_by_selenium(element_order_name).click()
        self.find_element_by_selenium(element_cargo).click()
        self.find_element_by_selenium(element_cargo_category).click()
        cargo_category = self.find_element_by_selenium(element_cargo_category)
        cargo_category.find_element(By.XPATH, value="//option[. = '重货']").click()

        self.find_element_by_selenium(element_order_weight).click()
        self.find_element_by_selenium(element_order_weight).send_keys('10')

        self.find_element_by_selenium(element_order_packing).click()
        order_packing = self.find_element_by_selenium(element_order_packing)
        order_packing.find_element(By.XPATH, "//option[. = '无']").click()

        self.find_element_by_selenium(element_vehicle_type_id).click()
        self.find_element_by_selenium(element_vehicle_no_limit).click()
        self.find_element_by_selenium(element_vehicle_type).click()

        self.find_element_by_selenium(element_carriage_length_id).click()
        self.find_element_by_selenium(element_carriage_length_no_limit).click()
        self.find_element_by_selenium(element_carriage_length).click()

        self.find_element_by_selenium(element_despatch_start).click()
        self._time_control_set('2020,10,27')

        self.find_element_by_selenium(element_despatch_end).click()
        self._time_control_set('2020,10,30')

        self.find_element_by_selenium(element_receipt_start).click()
        self._time_control_set('2020,10,31')

        self.find_element_by_selenium(element_cargo_money).click()
        self.find_element_by_selenium(element_cargo_money).send_keys('10000')

        self.find_element(By.CSS_SELECTOR, ".mr-30:nth-child(4) > .radio").click()
        self.find_element(By.ID, "quote").click()
        self.find_element(By.ID, "quote").send_keys("100")
        self.find_element(By.ID, "haveBuyPolicyYes").click()
        self.find_element(By.ID, "serviceAgreement").click()
        self.find_element(By.ID, "haveReceipt2").click()
        self.find_element(By.ID, "haveSupportSdOilCard2").click()
        self.find_element(By.LINK_TEXT, "货物不超长不超宽不超高").click()
        self.find_element(By.ID, "btn1").click()


if __name__ == '__main__':
    driver = Chrome()
    driver.open(url='/modules/mms/system/login.html')
    driver.login('17926661154', 'a123456789')
    driver.open_new_window_tab(url='http://sit.boss-admin.zczy.com/login.html')
    driver.login('mabeijing56', 'a123456')
    driver.change_window_tab(url='http://sit.zczy-web.zczy.com/modules/mms/system/login.html')
    driver.publish()
    driver.close()
    driver.quit()
