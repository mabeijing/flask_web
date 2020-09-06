# coding=utf-8
import winreg  # 和注册表交互
import re
import time
from selenium import webdriver


def getChromeVersion():
    version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本号的正则表达式
    try:
        # 从注册表中获得版本号
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Google\Chrome\BLBeacon')
        _v, type = winreg.QueryValueEx(key, 'version')

        print('Current Chrome Version: {}'.format(_v))  # 这步打印会在命令行窗口显示
        # return version_re.findall(_v)[0]  # 返回前3位版本号
        return _v
    except WindowsError as e:
        print('check Chrome failed:{}'.format(e))


version_ = getChromeVersion()

option = webdriver.ChromeOptions()
# option.add_argument("--headless")
# option.add_argument("--disable-gpu")
option.add_experimental_option('excludeSwitches', ['enable-automation'])
path = "D:\\chromedriver\\{version}\\chromedriver.exe".format(
    version=version_)
driver = webdriver.Chrome(options=option, executable_path=path)
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(1)
print(driver.capabilities)
driver.quit()

# # 新版Edge浏览器支持
# driver = webdriver.Edge(
#     executable_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe")
# driver.get("http://www.baidu.com/")
# time.sleep(1)
# print(driver.capabilities)
# driver.quit()

"""
set_options.add_argument('--headless')#设置无界面模式运行浏览器
set_options.add_argument('--start-maximized')#设置启动浏览器时窗口最大化运行
set_options.add_argument('--incognito')#设置无痕模式
set_options.add_argument('--disable-infobars')#设置禁用浏览器正在被自动化程序控制的提示
set_options.add_argument('--window-size=1928,1080')#设置浏览器分辨率窗口大小


options.add_experimental_option(‘excludeSwitches‘,[‘enable-automation‘])#去掉黄条


设置 chrome 二进制文件位置 (binary_location)
添加启动参数 (add_argument)
添加扩展应用 (add_extension, add_encoded_extension)
添加实验性质的设置参数 (add_experimental_option)
设置调试器地址 (debugger_address)
"""
