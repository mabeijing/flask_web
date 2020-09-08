from selenium import webdriver
import winreg
import os
import logging
import pytest


def get_chrome_driver():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
    _version, _version_type = winreg.QueryValueEx(key, 'version')
    print('Current Chrome Version: {}'.format(_version))
    dir_list = [item.split('.') for item in os.listdir('D:\chromedriver')]
    target_list = []
    for t_list in dir_list:
        # 比较chromedriver目录中文件夹名前3位等于系统chrome版本前3位的所有文件夹
        if t_list[:-1] == _version.split('.')[:-1]:
            target_list.append(t_list)
    if not target_list:
        raise ValueError('未找到对应的chromedriver')
    for index, item in enumerate(target_list):
        if item[3] == _version.split('.')[-1]:
            return '.'.join(target_list[index])
    return target_list[0]


class Test_demo:
    def setup_method(self, method):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # option.add_argument("--headless")
        # option.add_argument("--disable-gpu")
        path = "D:\\chromedriver\\{version}\\chromedriver.exe".format(version=get_chrome_driver())
        self.driver = webdriver.Chrome(options=option, executable_path=path)

    def teardown_method(self, method):
        self.driver.quit()

    def test_1(self):
        self.driver.get('https://www.baidu.com')
        print(self.driver.title)
        logging.error('ceshi')


if __name__ == '__main__':
    pytest.main(['-s'])
