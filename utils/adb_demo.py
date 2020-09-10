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


def check_devices():
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
        devices_dict[item.split('\t')[0]] = item.split('\t')[1]
    if not devices_dict:
        print('没数据')
    return devices_dict

devices_num = '127.0.0.1:21543'
# devices_num = 'NDF0217A28003675'
timestamp = time.localtime(time.time())
year = str(int(time.strftime('%Y', timestamp)))
month = str(int(time.strftime('%m', timestamp)))
day = str(int(time.strftime('%d', timestamp)))
target_month = year + '-' + month
target_day = month + '.' + day
source_dir = ' /sdcard/Pictures/Screenshots/'
target_dir = ' E:\\workshop\\Notes\\' + \
    target_month + '\\' + target_day + '\\bugimg'
res = check_devices()
if devices_num not in res.keys():
    print('输入的设备编号未连接adb，请检查')
    exit(505)
elif res[devices_num] != 'device':
    print('当前设备未准备好。状态为unauthorized')
    exit(505)


def get_pic():
    while not event.isSet():
        global flag
        all_files = os.popen('adb -s ' + devices_num +
                             ' shell ls' + source_dir)
        pic_list = [i[0:-1] for i in all_files][::2]
        if pic_list:
            for picture in pic_list:
                os.system('adb -s ' + devices_num + ' pull' +
                          source_dir + picture + target_dir)
                os.system('adb -s ' + devices_num + ' shell rm -rf' +
                          source_dir + picture)
            print('success!')
            if flag:
                event.set()
        else:
            print('wait')
            event.wait(timeout=3)


def run():
    thread1 = threading.Thread(target=get_pic)
    thread1.start()


def stop():
    global flag
    time.sleep(5)
    flag = True


if __name__ == '__main__':
    run()
