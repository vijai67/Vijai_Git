import paramiko
import time
from exceptions import AssertionError
from connections import connection

hostname = '192.168.0.19'
port = 22
username = 'root'
password = 'nexenta'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)
print "Connected To Nexenta Machine "
time.sleep(3)


def show_lun():
    cmd = "nmc -c 'show lun'"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    al = stdout.read()
    print(al)
    return (al)


total_lun=show_lun()


def show_volume():
    cmd = "nmc -c 'show volume'"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read())
    return (stdout)

total_volume=show_volume()


def check_lun(total_lun):
    lun1=[]

    for i in a.splitlines():
        x = [j for j in i.split(" ") if j!=""]

        if(x[0]!='c0t0d0' and len(x)==7):
            if(x[3]=='2GB'):
                lun1.append(x[0])

    return lun1
checking_lun=check_lun(total_lun)
print(checking_lun)


def create_volume(volume_name,a2):
    if(len(checking_lun)>=11):

        cmd = "nmc -c 'create volume " + volume_name  + " mirror " + a2[0] + " " + a2[1] + " " + "-y -y'"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read())
        time.sleep(5)
        cmd = "nmc -c 'create volume " + volume_name+"_1" + " raid5 " + a2[2] + " " + a2[3] + " " + "-y -y'"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read())
        time.sleep(5)
        cmd = "nmc -c 'create volume " + volume_name+"_2" + " raid6 " + a2[4] + " " + a2[5] + " " + a2[6] + " " + "-y -y'"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read())
        time.sleep(5)


d =create_volume("vol",checking_lun )
m=show_volume()
print(m)

def return_code(rc):
    if rc == 0:
        print "Command Executed Successfully"
    else:
        print "Command Terminated"
ssh.close()


class nfs:
    def __init__(self, ip='192.168.0.19'):
        self.ip = ip
        self.port = 22
        self.username = 'root'
        self.password = 'nexenta'
        self.command = []

    def nfsservice(self, ip='192.168.0.19', port=22, username='root', password='nexenta'):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        print ("Establish the connection")
        print ("check network service")
        self.command = ["nmc -c 'show network service'"]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password)

        try:
            stdin, stdout, stderr = ssh.exec_command("nmc -c 'setup network service nfs-server confcheck'")
            print stdout.readlines()
        except:
            print "no nfs service present,turning the nfs-server daemon"
        try:
            stdin, stdout, stderr = ssh.exec_command("nmc -c 'setup network service nfs-server enable'")
        except:
            print ("Unable to set nfs-server daemon plz do set")
        try:
            stdin, stdout, stderr = ssh.exec_command("nmc -c 'setup vol/ashwini share -n ash_ashwini -H '")

            print stdout.readlines()
        except:
            print ("no folder is present")


serv = nfs()
serv.nfsservice()
