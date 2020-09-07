"""
use py38_selenium interpreter
"""
import openpyxl
import os
import re
from bs4 import BeautifulSoup
import requests

"""
1、tailor()
    :param html_content
    :return soup.find_all()
"""
def get_html_content(url='https://npm.taobao.org/mirrors/chromedriver'):
    raw_data = requests.get(url)
    if not raw_data:
        raise ValueError('No Data Return!')
    return raw_data.content


# def tailor(content):
#     soup = BeautifulSoup(content, 'html.parser')
#     data_list = soup.find_all(href=re.compile("mirrors/chromedriver/\d+"))
#     result_set = [(element.attrs['href'], element.string) for element in data_list][:-1]
#     return result_set
def tailor(html, regx):
    soup = BeautifulSoup(html, 'html.parser')
    reopen_data = soup.find_all(href=re.compile(regx))
    if not reopen_data:
        raise ValueError('No Data Match!')
    return reopen_data


def check_and_create_dir(data: list):
    
    base_dir = 'D:\\chromedriver'
    local_dirs = [(base_dir + '\\' + ele[1], ele[1]) for ele in data]
    if not os.path.exists(base_dir):
        for dirs, name in local_dirs:
            os.makedirs(dirs)
            os.chdir(dirs)
            data_list = _pre_download_file(name)
            _download(data_list)


def _pre_download_file(dirs):
    base_url = 'https://npm.taobao.org/mirrors/chromedriver/'
    url = base_url + dirs
    result = get_html_content(url)
    soup = BeautifulSoup(result, 'html.parser')
    data_list = soup.find_all(href=re.compile("mirrors/chromedriver/\d+"))
    return data_list


def _download(require_data):
    base_url = 'https://npm.taobao.org'
    for data in require_data:
        print(base_url + data.attrs['href'], data.string)
        r = requests.get(base_url + data.attrs['href'])
        with open(str(data.string), 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    html_content = get_html_content()
    result = tailor(html_content)
    check_and_create_dir(result)
