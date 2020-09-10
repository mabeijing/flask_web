import paramiko

ssh = paramiko.SSHClient()  # 创建SSH对象
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
ssh.connect(hostname='172.20.20.203', port=22,
            username='sit', password='sit@2018New')  # 连接服务器

stdin, stdout, stderr = ssh.exec_command('cd /data/projects/oilcard-app ; tail -f oilcard-app.logoilcard-app.log -n')
# stdin为输入的命令
# stdout为命令返回的结果
# stderr为命令错误时返回的结果
res, err = stdout.read().decode('utf-8'), stderr.read()
result = res if res else err
print(result)
ssh.close()  # 关闭连接
