from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--headless")
option.add_argument("--disable-gpu")

path = "D:\\chromedriver\\{version}\\chromedriver.exe".format(version="85.0.4183.83")
driver = webdriver.Chrome(options=option, executable_path=path)

driver.get('http://www.baidu.com')

print(driver.title)

driver.quit()
