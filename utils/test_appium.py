# import uiautomator2 as u2
# d = u2.connect_usb('91cd9d13')
# d.make_toast('666', 3)
import time
import pytest
from appium import webdriver


# @pytest.mark.skipif(DEBUG is True, reason='不执行')
class TestAppium:
    def setup_method(self, method):
        desired_caps = {
            'platformName': device.get('platformName'),
            'platfromVersion': decice.get('platfromVersion'),
            'deviceName': device.get('deviceName'),
            'appPackage': 'com.tiema.zhwl_android',
            'appActivity': 'com.tiema.zhwl_android.MainActivity',
            'newCommandTimeout': '120',
            'noReset': 'true',
            # 'app': 'D:\\V2.8_te_cyf_new.apk',
            'udid': udid
        }
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def teardown_method(self, method):
        self.driver.quit()

    def test_1(self):
        xx = self.driver.get_window_size()['width']
        yy = self.driver.get_window_size()['height']
        print(xx, yy)
        time.sleep(1)


if __name__ == '__main__':
    pytest.main(['-s'])
