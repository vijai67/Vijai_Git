import re
import subprocess
import os
from collections import namedtuple


# function for running the linux commands
def run_cmd(cmd):
    try:
        cmd_result = namedtuple("result",["statuscode","output","error"])
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result.wait()
        out,err = result.communicate()
        return cmd_result(result.returncode, output=out, error=err)
    except Exception as e:
        return e


# function for printing all available disks
def available_disk():
    try:
        disks = run_cmd("lsblk /dev/sd[b-z] -o path -s -n")
        if disks.statuscode == 0:
            disk = disks.output.split("\n")
            tot_disk =[]
            for d in disk:
                if d != "":
                    tot_disk.append(d)
            return tot_disk
        else:
            raise Exception("No available disk")
    except Exception as e:
        return e


# apply the gpt table to disk
def apply_gpt(disk_name):
    try:
        gpt = subprocess.run(f"parted {disk_name} mktable gpt",shell=True,check=True)
        return gpt.returncode
    except Exception as e:
        return e

# function for creating primary partition each 1GB
def create_partition(disk_name):
    try:
        size = run_cmd(f"lsblk {disk_name} -o size -n -r")
        get_size = re.search(r"\d+",size.output)
        start = 0
        end = 1
        while end <= int(get_size.group()):
            mkpart = run_cmd(f"parted {disk_name} mkpart primary {start}G {end}G")
            start +=1
            end += 1
        return True
    except Exception as e:
        return e

# get available partition in disk
def availabel_partitions(disk_name):
    try:
        ava_part = run_cmd(f"lsblk {disk_name} -o path -n")
        part = str(ava_part.output)
        total_part = [i for i in part.split("\n") if i != ""]
        return {total_part[0] : total_part[1:]}
    except Exception as e:
        return e

# set the file system to the partition
def mkfile_sys(part_path, type):
    try:
        file_sys = run_cmd("mkfs -t {} {}".format(type,part_path))
        if file_sys.statuscode == 0:
            return True
        else:
            raise Exception(False)
    except Exception as e:
        return e

def Mounting(part_path, mount_path):
    try:
        mount = run_cmd("mount {} {}".format(part_path,mount_path))
        if mount.statuscode == 0:
            return True
        else:
            raise Exception(False)
    except Exception as e:
        return e

def Un_Mounting(part_path):
    try:
        unmount = run_cmd("umount {}".format(part_path))
        if unmount.statuscode == 0:
            return True
        else:
            raise Exception(False)
    except Exception as e:
        return e

def delete_partition(disk_name):
    try:
        del_part = run_cmd(f"partx --delete {disk_name}")
        if del_part.statuscode == 0:
            return True
        else:
            raise Exception(False)
    except Exception as e:
        return e
