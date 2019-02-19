# -*- coding:utf-8 -*-
import paramiko

host = "192.168.0.219"
port = 22
timeout = 30
user = "dkadmin"
password = "admin123"


def sftp_upload_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sftp_upload_file("/home/dkadmin/chiudk", r"C:\Users\Chiu\Desktop\chiudk")