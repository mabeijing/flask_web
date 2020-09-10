import time
import allure
import pytest
from selenium import webdriver


@allure.epic("测试大类")
@allure.feature("测试模块")
class TestDemo:
    def setup_method(self, method):
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        # option.add_argument("--disable-gpu")
        option.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        path = "E:\\chromeDriver\\85.0.4183.83\\chromedriver.exe"

        self.driver = webdriver.Chrome(options=option, executable_path=path)

    def teardown_method(self, method):
        self.driver.quit()

    @allure.step("步骤1")
    @allure.title("用例的标题")
    @allure.story("用户故事：1")
    def test_1(self):

        self.driver.get('https://www.baidu.com')

        time.sleep(10)
        print(self.driver.title)

    @allure.story("用户故事：2")
    def test_2(self):
        time.sleep(11)
        print('pass')
if __name__ == '__main__':
    pytest.main()
