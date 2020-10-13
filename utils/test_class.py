from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_experimental_option(
    'excludeSwitches', ['enable-automation'])
path = "D:\\chromedriver\\85.0.4183.83\\chromedriver.exe"

driver = webdriver.Chrome(options=option, executable_path=path, service_log_path='log.txt')

args = driver.service.command_line_args()
print(args)

driver.get('https://www.baidu.com')

driver.find_element(by='id', value='kw').send_keys('1234')

driver.quit()
