import os
import time

from os.path import isfile, join
while True:
    time.sleep(30)
    clientInputDir = "/home/matteo/Desktop/OutputData"
    tenantsappdir = "./clientbatchingestapps/"
    files = []
    for dir in os.walk(clientInputDir):
        if dir[0] != clientInputDir:
            if os.listdir(dir[0]):
                tenant = os.path.basename(os.path.normpath(dir[0]))
                for file in os.listdir(dir[0]):
                    files.append(dir[0] + '/'+ file)
                    os.system('python ' + tenantsappdir + 'clientbatchingestapp_' + os.path.basename(os.path.normpath(dir[0])) + '.py "' + dir[0] + '/'+ file + '"')
    for file in files:
        os.remove(file)

# TODO: multitreading
# TODO: logging and test
# TODO: microbatching solution