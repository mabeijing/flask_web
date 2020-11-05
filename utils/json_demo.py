import json
from json import JSONDecodeError

dict_raw_data = {
    "name": '小马',
    'sex': '男',
    'phone': None
}
json_raw_data_data = """{"name": "小刘", "sex": "女", "phone": null}"""

# 将dict转化成json
json_data = json.dumps(dict_raw_data, ensure_ascii=False)
print(json_data)

# 将json转化成dict
dict_data = json.loads(json_data)
print(dict_data)

# # 将dict转化成json并且写入文件
# with open('json_data.txt', 'w', encoding='utf-8') as f:
#     json.dump(dict_raw_data, f, ensure_ascii=False)
#
# # 从文件读取json文件转化成dict
# with open('json_data.txt', 'r') as f:
#     data = json.load(f)
# print(data)

