import time
import allure
import pytest
from selenium import webdriver


@allure.epic("测试大类")
@allure.feature("测试模块")
class TestDemo:
    """
    注意区别
    setup_method（self, method）
    每个case执行结束都会调用。必须穿method

    setup_class（self）
    类执行开始结束会调用，

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

    """

    def setup_class(self):
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        # option.add_argument("--disable-gpu")
        option.add_experimental_option(
            'excludeSwitches', ['enable-automation'])
        path = "D:\\chromedriver\\85.0.4183.83\\chromedriver.exe"

        self.driver = webdriver.Chrome(options=option, executable_path=path)

    def teardown_class(self):
        self.driver.quit()

    def locate_element(self, web_element):
        return self.driver.find_element(**web_element)

    @allure.step("步骤1")
    @allure.title("用例的标题")
    @allure.story("用户故事：1")
    def test_1(self):
        self.driver.get('https://www.baidu.com')

        time.sleep(2)
        print(self.driver.title)
        print(self.driver.session_id)

    @allure.story("用户故事：2")
    def test_2(self):
        element = {'by': 'id', 'value': 'kw'}
        self.locate_element(element).send_keys('1234')
        print(self.driver.session_id)
        time.sleep(2)
        print('pass')


if __name__ == '__main__':
    pytest.main(['-s'])
