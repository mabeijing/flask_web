import os
import time
import logging
import threading
import subprocess

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
event = threading.Event()
flag = False
"""
1、检查adb server是否启动成功：
    如果stderr存在 '* daemon started successfully' 表示启动成功。否则重启3次后失败报错。
2、获取所有连接设备，并记录状态device unauthorized
3、数据想要的设备号[未实现]，查询设备状态是否device，如果是，继续操作，如果不是，重启adb刷新状态
4、
"""


def restart_adb():
    killserver = subprocess.Popen(
        'adb kill-server', shell=True, stderr=subprocess.PIPE)
    try:
        err = killserver.stderr.read().decode('gbk')
    except UnicodeDecodeError:
        err = killserver.stderr.read().decode('utf-8')
    if err:
        print('%s\n执行错误,程序退出。' % err)
        exit(500)

    time.sleep(1)

    startserver = subprocess.Popen(
        'adb start-server', shell=True, stderr=subprocess.PIPE)
    try:
        stderr = startserver.stderr.read().decode('gbk')
    except UnicodeDecodeError:
        stderr = startserver.stderr.read().decode('utf-8')
        if 'successfully' in stderr:
            return True


def check_device(serial: str = None):
    fd = subprocess.Popen(['adb', 'devices'], shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    all_devices_list = fd.stdout.readlines()[1:-1]

    devices_dict = {}
    devices_list = []

    if not all_devices_list:
        return all_devices_list

    for item in all_devices_list:
        devices_dict['deviceName'] = item.split('\t')[0]
        devices_dict['deviceStatus'] = item.split('\t')[1].strip()
        devices_list.append(devices_dict.copy())

    logging.info(devices_list)

    if serial is None:
        return devices_list
    for item in devices_list:
        if item.get('deviceName') == serial and item.get('deviceStatus') == 'device':
            return True
    return False


def connect_device(serial: str):
    fd = subprocess.Popen(['adb', 'connect', serial], shell=True, stdout=subprocess.PIPE)
    out = fd.stdout.readline().decode('utf-8')
    logging.info(out)
    reason = 'cannot connect to {serial}: 由于目标计算机积极拒绝，无法连接。 (10061)'.format(serial=serial)
    if out.strip() == reason:
        raise ValueError(out)

    # check_device()


if __name__ == '__main__':
    # connect_device('192.168.8.200:7401')
    tag = check_device('8KE0219827001728')
    print(tag)
    check_device()