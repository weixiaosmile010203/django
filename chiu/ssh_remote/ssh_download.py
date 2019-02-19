# -*- coding:utf-8 -*-

host = "192.168.0.219"
port = 22
timeout = 30
user = "dkadmin"
password = "admin123"
import paramiko

def sftp_down_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path, local_path)
        t.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sftp_down_file("/home/dkadmin/test", r"C:\Users\Chiu\Desktop\test")