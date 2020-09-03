import pymongo

# 实例化
instance = pymongo.MongoClient("mongodb://192.168.8.200:27017")

# 创建一个数据库
db = instance['test']

# 查看当前数据库下所有的集合
print(db.list_collection_names())

# 使用db数据库下的['user_info']集合
user_info = db['user_info']

# 数据1
user1 = {
    "id": 2,
    "name": "橘右京",
    "age": 30
}

# 插入
user_info.insert_one(user1)

# 查询
result = user_info.find_one({"id": 2}, {"_id": 0})
print(result)
#
# tms_db = instance['tms_db']
# collection_data = tms_db['api']
# api1 = [{
#     "_id": 10,
#     "step": 1,
#     "method": "post",
#     "url": "https://www.baidu.com"
# }, {
#     "_id": 20,
#     "step": 2,
#     "method": "get",
#     "url": "https://www.baidu.com"
# }]
#
# collection_data.insert_many(api1)
