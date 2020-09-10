# import uiautomator2 as u2
# d = u2.connect_usb('91cd9d13')
# d.make_toast('666', 3)
import time
import pytest
from appium import webdriver
import subprocess
import requests
import random
import json
import time
TOKEN = '3d2a272b64174ea9a2338ee973285749e0c36fb11e00410b95da36553d4964f6'
BASE_URL = 'http://192.168.88.202:7100'
# DEVICES = 'CLB0218825010999'
DEBUG = True

default_header = {
    "Authorization": "Bearer {}".format(TOKEN)
}

headers = {
    "Content-Type": "application/json"
}
headers.update(default_header)


def get_all_devices():
    url_getDevices = BASE_URL + '/api/v1/devices'
    respone = requests.get(url=url_getDevices, headers=default_header)
    raw_dict_data = respone.json()['devices']
    devices_list = []
    devices_dict = {}
    for device in raw_dict_data:
        devices_dict['platformName'] = device.get('platform')
        devices_dict['platfromVersion'] = device.get('version')
        devices_dict['deviceName'] = device.get('product')
        devices_dict['udid'] = device.get('serial')
        devices_dict['using'] = device.get('using')
        devices_dict['present'] = device.get('present')
        devices_list.append(devices_dict.copy())
    return devices_list


def get_available_device(udid=None):
    devices_list = get_all_devices()
    if not devices_list:
        raise
    usable_devices = []
    for item in devices_list:
        if item['present'] and (not item['using']):
            usable_devices.append(item)

    if udid:
        # print(usable_devices)
        for item in usable_devices:
            if udid == item.get('udid'):
                return item
            else:
                return None
    else:
        return usable_devices


def connect_device(udid):
    subprocess.Popen('adb connect ' + udid, shell=True)


def check_devices(udid=None):
    # subprocess.Popen('adb connect 127.0.0.1:62027', shell=True)
    subs = subprocess.Popen(
        'adb devices', shell=True, stdout=subprocess.PIPE)
    try:
        all_devices = subs.stdout.read().decode('gbk')
    except UnicodeDecodeError:
        all_devices = subs.stdout.read().decode('utf-8')

    devices_dict = {}
    tmp_list = [dev for dev in all_devices.strip().split('\r\n')[1:]]
    for item in tmp_list:
        devices_dict['deviceName'] = item.split('\t')[0]
        devices_dict['deviceStatus'] = item.split('\t')[1]
    if not devices_dict:
        print('没数据')
    # print(devices_dict)
    return devices_dict


def obtain_device_permission(devices):
    headers = {
        "Content-Type": "application/json"
    }
    headers.update(default_header)
    data = {
        "serial": devices
    }
    url_userDevice = BASE_URL + '/api/v1/user/devices'
    r = requests.post(url=url_userDevice,
                      data=json.dumps(data), headers=headers)
    if r.json().get('success'):
        url_connectDevice = BASE_URL + \
            '/api/v1/user/devices/{serial}/remoteConnect'.format(
                serial=devices)
        r_connectDevice = requests.post(
            url=url_connectDevice, headers=default_header)
        result = r_connectDevice.json()
    else:
        release_device(device)
        result = {}
    # print(result)
    return result


def release_device(device):
    url_remoteConnect = BASE_URL + \
        '/api/v1/user/devices/{serial}/remoteConnect'.format(serial=device)
    r2 = requests.delete(url=url_remoteConnect, headers=default_header)
    print(r2.json())

    url_userDevice = BASE_URL + \
        '/api/v1/user/devices/{serial}'.format(serial=device)
    r = requests.delete(url=url_userDevice, headers=default_header)
    print(r.json())


available_device = get_available_device()

device = random.choice(available_device)
print(device)
udid = obtain_device_permission(device.get('udid')).get('remoteConnectUrl')
print(udid)


@pytest.mark.skipif(DEBUG is True, reason='不执行')
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
