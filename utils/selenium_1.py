from selenium import webdriver


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time


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

    def find_e(self, element):
        for key, value in element.__dict__.items():
            if value and key != 'js':
                try:
                    return self.find_element(by='css', value=value)
                except WebDriverException as e:
                    print(key, value, e)
            elif value and key == 'js':
                return self.execute_script(value)
            else:
                pass


class WebElement:
    def __init__(self, id=None, name=None, css=None, text=None, xpath=None):
        self.ID = id
        self.CSS_SELECTOR = css
        self.LINK_TEXT = text
        self.XPATH = xpath

exchange = {'css': '.tab-link:nth-child(2)', 'text': '账号登录', 'xpath': '//a[2]'}

element_exchange = WebElement(**exchange)

element_username = WebElement(id='userName')

element_password = WebElement(id='userPwd')


element_login = WebElement(id='memberLogin')


BASE_PR_URL = 'http://pre.zczy-web.zczy.com'


class Base:
    def __init__(self):
        pass

    def open(self, url=None):
        urls = BASE_PR_URL + url
        self.get(urls)


class Chrome(BaseChrome, Base):
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
        Base.__init__(self)

    # def open(self, url=None):
    #     urls = BASE_PR_URL + url
    #     self.get(urls)
    #     pass

    def login(self, username, password):
        try:
            self.find_e(element_exchange).click()
            self.find_e(element_username).send_keys(username)
            self.find_e(element_password).send_keys(password)
            self.find_e(element_login).click()
            if self.title == '我的智运-个人中心':
                self.save_screenshot('登陆成功图.png')
            else:
                self.save_screenshot('登陆失败.png')
        except Exception as e:
            print(e)
            self.save_screenshot('1.png')
            self.quit()

if __name__ == '__main__':
    # option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    # option.add_argument("--disable-gpu")
    from selenium import webdriver
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')
    driver = Chrome(options=option)
    driver.open(url='/modules/mms/system/login.html')
    driver.login('17916661005', 'a123456789')

    driver.quit()
