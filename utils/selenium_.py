from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Safari()
#
# driver.get('https://www.baidu.com')
#
# driver.find_element(by=By.ID, value='kw').send_keys('1234')
# driver.find_element(by=By.ID, value='su').click()
#
# time.sleep(1)
# driver.quit()

class Safari(webdriver.Safari):
    def __init__(self, port=0, executable_path="/usr/bin/safaridriver", reuse_service=False,
                 desired_capabilities=DesiredCapabilities.SAFARI, quiet=False,
                 keep_alive=True, service_args=None):
        super(Safari, self).__init__(port=port, executable_path=executable_path,
                                     reuse_service=reuse_service,
                                     desired_capabilities=desired_capabilities,
                                     quiet=quiet,
                                     keep_alive=keep_alive,
                                     service_args=service_args)

    def find_e(self, by=By.ID, value=None):
        return self.find_element(by=by, value=value)


driver = Safari()
driver.get('https://www.baidu.com')
driver.find_e(by=By.ID, value='kw').send_keys('1234')
driver.find_e(by=By.ID, value='su').click()
time.sleep(1)
driver.quit()
