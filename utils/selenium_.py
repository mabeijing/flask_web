from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time


class Chrome(webdriver.Chrome):
    def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
        super(Chrome, self).__init__(executable_path=executable_path,
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
                    return self.find_element(by=key, value=value)
                except WebDriverException as e:
                    print(key, value, e)
            elif value and key == 'js':
                return self.execute_script(value)
            else:
                pass


class WebElement:
    def __init__(self, id=None, name=None, css=None, xpath=None, js=None):
        self.id = None
        self.name = None


element_input = WebElement()
element_input.id = 'kwa'
element_input.name = 'wd'

element_click = WebElement()
element_click.id = 'su'
element_click.js = 'document.getElementById("su")'

element_alert = WebElement()
element_alert.js = 'alert("提示信息！")'

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_experimental_option(
    'excludeSwitches', ['enable-automation'])
path = "D:\\chromedriver\\85.0.4183.83\\chromedriver.exe"

driver = Chrome(options=option, executable_path=path)
driver.get('https://www.baidu.com')
driver.find_e(element_input).send_keys('1234')
driver.find_e(element_alert)
time.sleep(1)
driver.switch_to.alert.accept()
driver.find_e(element_click).click()
time.sleep(1)
driver.quit()
