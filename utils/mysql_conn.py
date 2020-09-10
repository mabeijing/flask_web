import pymysql
version = pymysql.get_client_info()


mysql_conf = {
    "host": "192.168.8.200",      # 要连接的主机地址
    "user": "root",               # 用于登录的数据库用户
    "password": "Root@123",       # 密码
    "database": "mms_db",         # 要连接的数据库
    "port": 3306,                 # 端口，一般为 3306
    "unix_socket": None,          # 选择是否要用unix_socket而不是TCP/IP
    "charset": "utf8mb4"          # 字符编码
}

connect = pymysql.Connect(**mysql_conf)
cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute(
    'select * from user where ID = {id}'.format(id=3))
result = cursor.fetchone()
print(result)
