"""
用于windows操作adb
1、操作adb服务

"""
__version__ = '1.0'

import subprocess
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class PyAdb:
    @classmethod
    def check_adb_status(cls):
        fd = subprocess.Popen(['adb', 'devices'], shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        err = fd.stderr.read().decode('gbk')
        if err:
            raise ValueError(err)
        print('*' * 30)
        out = fd.stdout.read().decode('gbk')
        logging.info(out)


if __name__ == '__main__':
    PyAdb.check_adb_status()
