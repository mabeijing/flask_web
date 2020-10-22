import pymongo
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://owner.zczy56.com/'
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


class Functions:

    def open(self, url=None):
        urls = BASE_URL + url
        self.get(urls)
        self.maximize_window()


class Chrome(BaseChrome, Functions):
    """docstring for Login"""

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

    # def open(self, url=None):
    #     urls = BASE_PR_URL + url
    #     self.get(urls)
    #     pass
    def __enter__(self):
        time.sleep(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.switch_to.parent_frame()

    def login(self, user_name, password):
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
        self.switch_to.frame(0)
        time.sleep(0.5)
        self.find_element(By.XPATH, "//td[@onclick='day_Click(2020,10,24);']").click()
        ele1 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]")
        self.execute_script("arguments[0].focus();", ele1)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]").send_keys('9')
        ele2 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]")
        self.execute_script("arguments[0].focus();", ele2)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]").send_keys('55')
        self.find_element(By.XPATH, '//input[@id="dpOkInput"]').click()
        self.switch_to.parent_frame()

        self.find_element_by_selenium(element_despatch_end).click()
        self.switch_to.frame(0)
        time.sleep(0.5)
        self.find_element(By.XPATH, "//td[@onclick='day_Click(2020,10,30);']").click()
        ele1 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]")
        self.execute_script("arguments[0].focus();", ele1)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]").send_keys('9')
        ele2 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]")
        self.execute_script("arguments[0].focus();", ele2)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]").send_keys('55')
        self.find_element(By.XPATH, '//input[@id="dpOkInput"]').click()
        self.switch_to.parent_frame()

        self.find_element_by_selenium(element_receipt_start).click()
        self.switch_to.frame(0)
        time.sleep(0.5)
        self.find_element(By.XPATH, "//td[@onclick='day_Click(2020,10,31);']").click()
        ele1 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]")
        self.execute_script("arguments[0].focus();", ele1)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[1]").send_keys('9')
        ele2 = self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]")
        self.execute_script("arguments[0].focus();", ele2)
        self.find_element(By.XPATH, "//div[@id='dpTime']/table/tbody/tr/td/input[3]").send_keys('55')
        self.find_element(By.XPATH, '//input[@id="dpOkInput"]').click()
        self.switch_to.parent_frame()

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
    from selenium import webdriver

    option = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    option.add_experimental_option('prefs', prefs)  # 关掉浏览器左上角的通知提示，如上图
    option.add_argument("disable-infobars")  # 关闭'chrome正受到自动测试软件的控制'提示
    driver = Chrome(options=option)
    driver.open(url='/modules/mms/system/login.html')
    driver.login()
    driver.publish()

    driver.quit()
