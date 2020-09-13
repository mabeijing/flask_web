import requests
import json
TOKEN = '3d2a272b64174ea9a2338ee973285749e0c36fb11e00410b95da36553d4964f6'
BASE_URL = 'http://192.168.88.202:7100'
DEVICES = 'CLB0218825010999'

default_header = {
    "Authorization": "Bearer {}".format(TOKEN)
}


# # GET /api/v1/devices
# url_getDevices = BASE_URL + '/api/v1/devices'
# respone = requests.get(url=url_getDevices, headers=default_header)
# # print(respone.json()['devices'])
# for devices in respone.json()['devices']:
#     print('-----------------------')
#     print(devices)

# # GET /devices/{serial}
# url_getDevice = BASE_URL + '/api/v1/devices/{serial}'.format(serial=DEVICES)
# respone = requests.get(url=url_getDevice, headers=default_header)
# print(respone.json())

# # GET /api/v1/user
# # 查看当前用户绑定key得
# url_user = BASE_URL + '/api/v1/user'
# respone = requests.get(url=url_user, headers=default_header)
# print(respone.json())

# # GET /api/v1/user/devices
# # 查看名下设备
# url_userDevices = BASE_URL + '/api/v1/user/devices'
# respone = requests.get(url=url_userDevices, headers=default_header)
# print(respone.json())


# POST /api/v1/user/devices
# 占用设备
# headers = {
#     "Content-Type": "application/json"
# }
# headers.update(default_header)
# data = {
#     "serial": DEVICES
# }
# url_userDevice = BASE_URL + '/api/v1/user/devices'
# r = requests.post(url=url_userDevice, data=json.dumps(data), headers=headers)
# print(r.json())

# # POST /api/v1/user/devices/{serial}/remoteConnect
# # 连接远程设备，必须先占用
# url_connectDevice = BASE_URL + \
#     '/api/v1/user/devices/{serial}/remoteConnect'.format(serial=DEVICES)
# r_connectDevice = requests.post(url=url_connectDevice, headers=default_header)
# print(r_connectDevice.json())


# # DELETE /api/v1/user/devices/{serial}/remoteConnect
# # 释放远程设备
# url_remoteConnect = BASE_URL + \
#     '/api/v1/user/devices/{serial}/remoteConnect'.format(serial=DEVICES)
# r2 = requests.delete(url=url_remoteConnect, headers=default_header)
# print(r2.json())

# # DELETE /api/v1/user/devices/{serial}
# # 移除设备占用
# url_userDevice = BASE_URL + \
#     '/api/v1/user/devices/{serial}'.format(serial=DEVICES)
# r = requests.delete(url=url_userDevice, headers=default_header)
# print(r.json())
