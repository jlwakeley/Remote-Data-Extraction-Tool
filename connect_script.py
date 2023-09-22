#!/usr/bin/env python3

import paramiko

# write host IP, username, and password
host = ""
usr = ""
pwd = ""

# establish remote connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=usr, password=pwd)


sftp = ssh.open_sftp()

# Transfer script to the remote computer, path and local path need to be specified.
path = "enter receipt path here"
localpath = "enter local path of execute.py here"
sftp.put(localpath, path)

# Run the script
stdin, stdout, stderr = ssh.exec_command("""execute.py""")

# return the output. Must specify return path.
sftp.get(
    "enter path to the file to send",
    "enter destination of file on local",
)

# close connection
sftp.close()
ssh.close()
