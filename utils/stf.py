"""
整合stf调用方法
"""
import requests
import json


class STF:
    def __init__(self, token,
                 base_url='http://localhost:7100', debug=False):
        self.token = token
        self.base_url = base_url
        self.debug = debug
        self.default_headers = {"Authorization": "Bearer {}".format(token)}

    @staticmethod
    def __do_dict_data(t_dict: dict, s_dict: dict, t_list: list) -> None:
        t_dict['platformName'] = s_dict.get('platform')
        t_dict['platformVersion'] = s_dict.get('version')
        t_dict['deviceName'] = s_dict.get('product')
        t_dict['udid'] = s_dict.get('serial')
        t_dict['using'] = s_dict.get('using')
        t_dict['present'] = s_dict.get('present')
        t_list.append(t_dict.copy())

    def get_device(self, serial: str = None) -> list:
        """
        1、不带serial返回所有devices
        2、带serial，返回单个device
        """
        device_list = []
        devices_dict = {}
        if serial is None:
            url_get_device = self.base_url + '/api/v1/devices'
        else:
            url_get_device = self.base_url + '/api/v1/devices/{serial}'.format(serial=serial)
        response = requests.get(url=url_get_device, headers=self.default_headers)
        try:
            """
            验证返回值如果非json格式，则认为数据返回失败，return 空数组
            """
            result = response.json()
        except json.JSONDecodeError:
            return device_list

        """
        过滤返回False
        根据serial区分判断
        """
        if result.get('success') is False:
            return device_list

        if serial is None:
            raw_data_dict = result.get('devices')
            for raw_data in raw_data_dict:
                self.__do_dict_data(devices_dict, raw_data, device_list)
        else:
            raw_data = result.get('device')
            self.__do_dict_data(devices_dict, raw_data, device_list)

        return device_list

    def use_device_status(self, serial: str) -> dict:
        """获取设备的使用状态，如果可以使用，则占用设备"""
        headers = {"Content-Type": "application/json"}
        headers.update(self.default_headers)
        data = {"serial": serial}
        url_use_device = self.base_url + '/api/v1/user/devices'

        r = requests.post(url=url_use_device, data=json.dumps(data), headers=headers)
        try:
            result = r.json()
        except json.JSONDecodeError as e:
            raise RuntimeError(e)
        print(result)
        return result

    def connect_device(self, serial: str) -> dict:
        """连接设备前，必须先成功占用设备"""
        url_connect = self.base_url + '/api/v1/user/devices/{serial}/remoteConnect'.format(serial=serial)
        response = requests.post(url=url_connect, headers=self.default_headers)
        try:
            result = response.json()
        except json.JSONDecodeError as e:
            raise RuntimeError(e)
        print(result)
        return result

    def disconnect_device(self, serial: str) -> dict:
        url_remote = self.base_url + '/api/v1/user/devices/{serial}/remoteConnect'.format(serial=serial)
        response = requests.delete(url=url_remote, headers=self.default_headers)
        try:
            result = response.json()
        except json.JSONDecodeError as e:
            raise RuntimeError(e)
        print(result)
        return result

    def release_device(self, serial: str) -> dict:
        url_release = self.base_url + '/api/v1/user/devices/{serial}'.format(serial=serial)
        response = requests.delete(url=url_release, headers=self.default_headers)
        try:
            result = response.json()
        except json.JSONDecodeError as e:
            raise RuntimeError(e)
        print(result)
        return result


if __name__ == '__main__':
    import random
    TOKEN = '217a6998d1c4441aa1ca373e5e560430e90116985d6a407c846db2f4f606a723'
    BASE_URL = 'http://192.168.8.200:7100'
    stf = STF(token=TOKEN, base_url=BASE_URL)
    device_pools = stf.get_device()
    device = random.choice(device_pools)
    if device.get('present') and (not device.get('using')):
        serial_no = device.get('udid')
        print(device)
    else:
        raise ValueError()
    status = stf.use_device_status(serial_no)
    stf.connect_device(serial_no)
    stf.get_device(serial_no)
    # stf.disconnect_device(serial_no)
    # stf.release_device(serial_no)
