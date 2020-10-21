import pymongo
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time

mongo_conf = 'mongodb://192.168.8.200:27017'

# 实例化
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


exchange = element.find_one({'name': '账号登录'}, {"_id": 0})['element']
element_exchange = WebElement(**exchange)

username = element.find_one({'name': '用户名'}, {"_id": 0})['element']
element_username = WebElement(**username)

userPwd = element.find_one({'name': '密码'}, {"_id": 0})['element']
element_password = WebElement(id='userPwd')

memberLogin = element.find_one({'name': '登录按钮'}, {"_id": 0})['element']
element_login = WebElement(id='memberLogin')

BASE_URL = 'https://owner.zczy56.com/'


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

    def login(self, username, password):
        try:
            self.find_element_by_selenium(element_exchange).click()
            self.find_element_by_selenium(element_username).send_keys(username)
            self.find_element_by_selenium(element_password).send_keys(password)
            self.find_element_by_selenium(element_login).click()
            if self.title != '我的智运-个人中心':
                self.save_screenshot('登陆失败.png')
        except Exception as e:
            print(e)
            self.save_screenshot('1.png')
            self.quit()

    def publish(self):
        element_publish = WebElement(text='发布运单')
        self.find_element_by_selenium(element_publish).click()

        element_order_name = WebElement(name='orderName')
        self.find_element_by_selenium(element_order_name).click()

        element_cargo = WebElement(xpath="//span[contains(.,'无烟煤')]")
        self.find_element_by_selenium(element_cargo).click()

        element_cargo_category = WebElement(id='cargoCategory')
        self.find_element_by_selenium(element_cargo_category).click()

        dropdown = self.find_element_by_selenium(element_cargo_category)
        dropdown.find_element(By.XPATH, value="//option[. = '重货']").click()

        self.find_element(By.ID, "cargoCategory").click()
        self.find_element(By.NAME, "orderWeight").click()
        self.find_element(By.NAME, "orderWeight").send_keys("10")
        # self.find_element(By.ID, "orderPacking1").click()
        # dropdown = self.find_element(By.ID, "orderPacking1")
        # dropdown.find_element(By.XPATH, "//option[. = '无']").click()
        # self.find_element(By.ID, "orderPacking1").click()
        # self.find_element(By.ID, "vehicleTypeId").click()
        # self.find_element(By.CSS_SELECTOR, ".li:nth-child(1) > label > .checkbox").click()
        # self.find_element(By.CSS_SELECTOR, "#baseBlockDiv .li-row:nth-child(3)").click()
        # self.find_element(By.ID, "carriageLengthId").click()
        # self.find_element(By.CSS_SELECTOR, ".li:nth-child(1) > label > .checkbox").click()
        # self.find_element(By.CSS_SELECTOR,
        #                   "#baseBlockDiv .li-row:nth-child(3) > .li-item:nth-child(1) .title-text").click()
        # self.find_element(By.ID, "despatchStart").click()
        # self.switch_to.frame(0)
        # time.sleep(1)
        # self.find_element(By.XPATH, "//td[@onclick='day_Click(2020,10,22);']").click()
        # self.find_element(By.ID, "dpOkInput").click()
        # self.switch_to.default_content()
        # self.find_element(By.ID, "despatchEnd").click()
        # self.switch_to.frame(0)
        # self.find_element(By.CSS_SELECTOR, ".WdayOn").click()
        # self.find_element(By.ID, "dpOkInput").click()
        # self.switch_to.default_content()
        # self.find_element(By.ID, "despatchEnd").send_keys("2020-10-30 23:07")
        # self.find_element(By.ID, "receiptStart").click()
        # self.switch_to.frame(0)
        # self.find_element(By.CSS_SELECTOR, ".WwdayOn").click()
        # self.find_element(By.ID, "dpOkInput").click()
        # self.switch_to.default_content()
        # self.find_element(By.ID, "cargoMoney").click()
        # self.find_element(By.ID, "cargoMoney").send_keys("10000")
        # self.find_element(By.CSS_SELECTOR, ".mr-30:nth-child(4) > .radio").click()
        # self.find_element(By.ID, "quote").click()
        # self.find_element(By.ID, "quote").send_keys("100")
        # self.find_element(By.ID, "haveBuyPolicyYes").click()
        # self.find_element(By.ID, "serviceAgreement").click()
        # self.find_element(By.ID, "haveReceipt2").click()
        # self.find_element(By.ID, "haveSupportSdOilCard2").click()
        # self.find_element(By.LINK_TEXT, "货物不超长不超宽不超高").click()
        # self.find_element(By.ID, "btn1").click()


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
