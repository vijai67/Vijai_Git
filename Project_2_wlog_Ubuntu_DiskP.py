import subprocess
import logging

logging.basicConfig(level = logging.DEBUG,filename="logfile.log",format = "%(name)s - %(asctime)s - %(levelname)s - %(message)s")

class Disk_Partition:
	def __init__(self,device_name):
		self.device_name = device_name

	def Label_Part (self,device_gpt):
		logging.debug("PARTITION LABELING")
		s1 = subprocess.run(f"parted {self.device_name} mklabel {device_gpt} -y",shell=True)
		if s1.returncode != 0:
			logging.error(s1.stderr)

		else:
			logging.info("PARTITION LABELING DONE")

	def New_Partition(self,device_type,start,end):
		'''CREATING NEW PARTITION'''
		logging.debug("CREATING NEW PARTITION")
		part = subprocess.run(f"parted -a opt {self.device_name} mkpart primary {device_type} {start} {end}",shell=True)

		if part.returncode != 0:
			logging.info("PARTITION DELETING")
			Delete_Part = subprocess.run(f"parted {self.device_name} rm {partition_number}",shell=True)
			D = subprocess.run(f"hdparm -z {'/dev/sd[b-z]'}")
			logging.error(Delete_Part.stderr)
		
		elif part.returncode == 0:
			logging.error(part.stderr)
			logging.info("PARTITION DELETED")
		else:
			logging.info("PARTITION DONE")
			

	# def Delete_Partition(self,partition_number:int):
		'''DELETE THE EXISTING PARTITION'''
		# logging.debug("PARTITION DELETING")
		# Delete_Part = subprocess.run(f"parted {self.device_name} rm {partition_number}",shell=True)

		# if Delete_Part.returncode != 0:
		# 	D = subprocess.run(f"hdparm -z {['/dev/sd[b-z]']}")
		# 	logging.error(Delete_Part.stderr)

		# else:
		# 	logging.info("PARTITION DELETED")
		# 	D1 = subprocess.run(f"hdparm -z {['/dev/sd[b-z]']}")

	def Part_Details(self):
		'''DISK PARTITION DETAILS'''
		logging.debug("DISK PARTITION DETAILS")
		Detail = subprocess.run (f"fdisk -l {self.device_name}",shell=True)

		if Detail.returncode != 0:
			logging.error(Detail.stderr)

		else:
			logging.info("PARTITION DETAILS")

	def File_System (self,partition_type,partition_name):
		'''SELECTING FILE SYSTEM LIKE ext2, ext3, ext4'''
		logging.debug("FILE SYSTEM CREATING")
		file = subprocess.run (f"mkfs -t {partition_type} {partition_name}",shell=True)

		if file.returncode != 0:
			logging.error(file.stderr)

		else:
			logging.info("FORMATTED")

	def Mount_Disk (self,partition_name,mount_directory):
		'''MOUNTING THE DISK PARTITION TO A DIRECTORY'''
		logging.debug("MOUNTING THE DISK")
		mount = subprocess.run (f"mount {partition_name} {mount_directory}",shell=True,capture_output=True)

		if mount.returncode != 0:
			logging.error(mount.stderr)

		else:
			logging.info("DISK MONTED")

if __name__ == "__main__":
	x = Disk_Partition("/dev/sdb")

	x.Label_Part("gpt")
	x.New_Partition("ext4","0%","40%")
	x.New_Partition("ext4","20%","40%")
	x.New_Partition("ext4","40%","60%")
	x.New_Partition("ext4","60%","80%")
	x.New_Partition("ext4","80%","100%")

	#x.Delete_Partition("")

	#x.Part_Details()

	x.File_System("ext4","/dev/sdb1")
	#x.File_System("ext4","/dev/sdb2")
	x.File_System("ext4","/dev/sdb3")
	x.File_System("ext4","/dev/sdb4")
	x.File_System("ext4","/dev/sdb5")
	# x.File_System("ext4","/dev/sdb6")

	x.Mount_Disk("/dev/sdb1","/mnt/SAE")
	x.Mount_Disk("/dev/sdb3","/mnt/SAE1")
	x.Mount_Disk("/dev/sdb4","/mnt/SAE2")
	x.Mount_Disk("/dev/sdb5","/mnt/SAE3")
	# x.Mount_Disk("/dev/sdb6","/mnt/SAE4")
	x.Part_Details()
