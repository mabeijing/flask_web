import pymongo

mongo_conf = 'mongodb://192.168.8.200:27017'

# 实例化
instance = pymongo.MongoClient(mongo_conf)

if __name__ == '__main__':
    # 创建一个数据库
    db = instance['selenium']

    # 使用db数据库下的['WebElement']集合
    element = db['WebElement']

    elements_list = [
        {'id': 1,
         'name': '账号登录',
         'element': {'css': '.tab-link:nth-child(2)', 'text': '账号登录', 'xpath': '//a[2]'}},
        {'id': 2,
         'name': '用户名',
         'element': {'id': 'userName'}},
        {'id': 3,
         'name': '密码',
         'element': {'id': 'userPwd'}},
        {'id': 4,
         'name': '登录按钮',
         'element': {'id': 'memberLogin'}},
        {'id': 5,
         'name': '发布运单',
         'element': {'text': '发布运单', 'css': '#leftMenuLi60 > .li-text', 'xpath': "//div[@id='leftMenuLi60']/a"}},
        {'id': 6,
         'name': '货物名称',
         'element': {'name': 'orderName'}},
        {'id': 7,
         'name': '无烟煤',
         'element': {'css': 'li:nth-child(3) > .first-address', 'xpath': '//li[3]/span'}},
        {'id': 8,
         'name': '货物计量',
         'element': {'id': 'cargoCategory', 'name': 'cargoCategory', 'css': '#cargoCategory'}},
        {'id': 9,
         'name': '货物吨位',
         'element': {'name': 'orderWeight', 'css': '#orderWeight > .text', 'xpath': "//input[@name='orderWeight']"}},
        {'id': 10,
         'name': '货物包装',
         'element': {'id': 'orderPacking1', 'name': 'orderPacking', 'css': '#orderPacking1',
                     'xpath': "//select[@id='orderPacking1']"}},
        {'id': 11,
         'name': '车辆类型',
         'element': {'id': 'vehicleTypeId', 'name': 'vehicleTypeId', 'css': '#vehicleTypeId'}},
        {'id': 12,
         'name': '不限车辆',
         'element': {'css': '.li:nth-child(1) > label > .checkbox', 'xpath': '//li/label/input'}},
        {'id': 13,
         'name': '车长类型',
         'element': {'id': 'carriageLengthId', 'name': 'carriageLengthId'}},
        {'id': 14,
         'name': '不限车长',
         'element': {'css': '.li:nth-child(1) > label > .checkbox', 'xpath': '//li/label/input'}},
        {'id': 15,
         'name': '最早到场时间',
         'element': {'id': 'despatchStart', 'xpath': "//input[@id='despatchStart']"}},
        {'id': 16,
         'name': '最晚到场时间',
         'element': {'id': 'despatchEnd', 'name': 'despatchEndTime', 'css': '#despatchEnd',
                     'xpath': '//input[@id="despatchEnd"]'}},
        {'id': 17,
         'name': '收货时间',
         'element': {'id': 'receiptStart', 'name': 'receiptStartTime', 'css': '#receiptStart',
                     'xpath': '//input[@id="receiptStart"]'}},
        {'id': 18,
         'name': '整车货值',
         'element': {'id': 'cargoMoney', 'name': 'cargoMoney', 'css': '#cargoMoney',
                     'xpath': '//input[@id="cargoMoney"]'}},
        {'id': 19,
         'name': '',
         'element': {}},
        {'id': 20,
         'name': '',
         'element': {}},

    ]
    element.insert_many(elements_list)

    # # 数据1
    # user1 = {
    #     "id": 2,
    #     "name": "橘右京",
    #     "age": 30
    # }
    # # 插入
    # user_info.insert_one(user1)
    #
    # # 查询
    # result = user_info.find_one({"id": 2}, {"_id": 0})
    # print(result)
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
