from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

PKCS7_BLOCK_SIZE = AES.block_size
PKCS5_BLOCK_SIZE = 8

raw_data = [-41, -15, -35, -94, 76, 48, -28,
            64, -121, -67, -114, 18, 31, -125, -35, -109]
data = [i + 256 if i < 0 else i for i in raw_data]
iv = bytes(16)

message = '{"androidId":"c2a5f2b10fd596e8","appType":"2","darkPhysicsInfo":"-1205984509994147694","deviceMac":"FE:EB:42:A8:73:4B","loginName":"17926662121","loginPassword":"00000000","logianType":"1","mac":"58569334c2a5f2b10fd596e8865242585622832","physicsInfo":"2060113919968585669","relationFlag":"3","serialNo":"58569334","ostype":"and","bang_imei":"58569334","bang_mac":"fe:eb:42:a8:73:4b","model":"VOG-AL00","sdk":"25","bang_serviceTime":"1604484815940","mod":"HUAWEI","checkcode":"82d5ad2aaf4c373de489d239c7293d4e"}'

text = pad(message.encode('utf-8'), PKCS5_BLOCK_SIZE)

keys = bytearray(data)
cca = AES.new(key=keys, mode=AES.MODE_CBC, iv=iv)
res = cca.encrypt(text)
d = base64.b64encode(res).decode('utf-8')
print(d)

mess = '6GKQr1iM8FblvOha26QEOtnJQn3/QGzAMzOoHCJ5w6a3psFEy8cVanigDSPyUrpIjg2oUDSHD467QdNkS7nG73dP1DKvVcPF4PhOopJxF5iJLeMpp2xJ2Ir+Hx1PWCW49KEeln/1gDeSRs0qESpDFJLIut9J0y5cKf89EPssxBPJrKaGd60iqOYqIWOgaen7daYq9PYM7+xJxVE+NIMC74NrYnUn45FymPlmL+ebFs6EMSUmEHFGwtgVvNOr7lNYoFHSbbnttXGF45//6vBi+Srx5LeALDHAocYVfWOriVrijiGDMwbjAMxo+Nl5F98H07mdBzUWCYlKymoUxE+fD89uYyog3c2o+29o6cVSdIJJHuLnJLaxudc6uQYDhdci501E08BPW2AKix0N85wGVaIbWXhOzv3WNMqoEKfIwpVHPu5XozQ/TMYEMkWRAe4OsLmZ9mW3RPIFcOBm2+8r8LDOiYbHTD8RYGfyy/N9seQ336bUha7t/2AvYYD2OxLpMXdULKXuqD0DhjWVC6fyBtyM/qJkrt5vB5idB0WAzlzznAto8909pRoqGd5hM4hEKglbJXiZxD3v8/0yAXkXLuVUkZzVWNYCqWRaGGXdSjuk1F25xs7csCmwa1WCe3N1AxjOiPKBPsdXqONgqGDsk56tF2BQA1w1Z8J5XPsoxNQ='

temp = base64.b64decode(mess)

ccaa = AES.new(key=keys, mode=AES.MODE_CBC, iv=iv)
s = ccaa.decrypt(temp)
data = unpad(s, PKCS5_BLOCK_SIZE)
print(data.decode('utf-8'))
