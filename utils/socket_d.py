import socket
import struct

socket_demo = socket.socket()
socket_demo.connect(('localhost', 1313))

data = socket_demo.recv(24)
s = struct.unpack("<2b5ibB", data)
print(s)

data1 = socket_demo.recv(4)
s1 = struct.unpack("i", data1)
print(s1)
data_len = s1[0]
print(data_len)
da = b''
while True:
    da = da + socket_demo.recv(1000)
    if len(da) == data_len:
        break

print(len(da))
with open('1.jpg', 'wb+') as f:
    f.write(da)
