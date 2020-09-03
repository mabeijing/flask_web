import redis

config = {
    "host": "192.168.8.200",
    "password": "Root@123",
    "port": 6379,
    "db": 0,
    "decode_responses": True,  # 转化字符串，False是字节
    "encoding": "utf-8",
    "encoding_errors": "strict"
}

pool = redis.ConnectionPool(**config)

conn = redis.Redis(connection_pool=pool)

conn.set('cookie', '橘右京', 10)

print(conn.get('cookie'))
