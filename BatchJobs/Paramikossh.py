'''
Paramiko is library to connect to linux server.
'''
import csv
import paramiko as paramiko
from Utilities.configurations import *

# get details of properties.ini file from configurations file->getconfig()
username = getconfig()['server']['username']
password = getconfig()['server']['password']
port = getconfig()['server']['port']
host = getconfig()['server']['serverHost']

# to connect to linux server using the above details.
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# run commands on server
stdin, stdout, stderr = ssh.exec_command("ls -a")
print(stdout.readlines())  # folder names will be displayed

stdin, stdout, stderr = ssh.exec_command("cat demofile")
print(stdout.readlines())  # ["hello how are you ?\n", "7\n","56.5\n"]

# upload files to server, eg: script.py file will be uploaded.
sftp = ssh.open_sftp()

localpath = "C:\\Users\\VARUN\\Desktop\\Varun_Personal\\Automation_API\\BatchJobs\\script.py"
destpath = "script.py"

sftp.put(localpath, destpath)

# upload csv file to server, eg: csv file will be uploaded.
localpath2 = "C:\\Users\\VARUN\\Desktop\\Varun_Personal\\Automation_API\\BatchJobs\\loanasa.csv"
destpath2 = "loanasa.csv"

sftp.put(localpath2, destpath2)

# execute batch file-script.py file to upload values in csv file.
stdin, stdout, stderr = ssh.exec_command("python script.py")


# download files from server to local.
sftp.get("loanasa.csv","C:\\Users\\VARUN\\Desktop\\Varun_Personal\\Automation_API\\BatchJobs\\outputloans.csv")

#parse output csv file
with open("C:\\Users\\VARUN\\Desktop\\Varun_Personal\\Automation_API\\BatchJobs\\outputloans.csv") as f1:
    csvreader=csv.reader(f1,delimiter=',')
    for row in csvreader:
        if row[0]=="32321":
           assert row[1]=="rejected"



ssh.close() # close the ssh connection

