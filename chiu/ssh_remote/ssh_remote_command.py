# -*- coding:utf-8 -*-
import paramiko

host = "192.168.0.219"
port = 22
timeout = 30
user = "dkadmin"
password = "admin123"

def sftp_exec_command(command):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, 22, user, password)
        std_in, std_out, std_err = ssh_client.exec_command(command)
        for line in std_out:
            print(line.strip("\n"))
        ssh_client.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sftp_exec_command("netstat -utpln |grep 17044 |awk {'print $4'} |awk -F ':' {'print $2'};echo $?")