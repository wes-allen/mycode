#'!/usr/bin/env python3
##Moving files with sftp

##import paramiko so we can talk to SSH

import paramiko
import os

## where to connect to

t = paramiko.Transport("10.10.2.3", 22)  ## IP and port


## how to connnect

t.connect(username="bender", password="alta3")


##Make an sftp connection object

sftp = paramiko.SFTPClient.from_transport(t)

##iterate across the files within directory

for x in os.listdir("/home/student/filestocopy/"):  #iterate on directory contents
    if not os.path.isdir("/home/student/filestocopy/"+x):  # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

##close connection
sftp.close() #close the connection




