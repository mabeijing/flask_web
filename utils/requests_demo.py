import requests

r = requests.get(url='https://www.baidu.com/')

print(r.encoding)
r.encoding = 'utf-8'
print(r.content)