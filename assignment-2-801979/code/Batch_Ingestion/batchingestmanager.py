import os


from os.path import isfile, join

clientInputDir = "/home/matteo/Desktop/OutputData"
tennantsappdir = "./clientbatchingestapps/"
for dir in os.walk(clientInputDir):
    if dir[0] != clientInputDir:
        if os.listdir(dir[0]):
            tennant = os.path.basename(os.path.normpath(dir[0]))
            for file in os.listdir(dir[0]):
                os.system('python ' + tennantsappdir + 'clientbatchingestapp_' + os.path.basename(os.path.normpath(dir[0])) + '.py ' + dir[0] + '/'+ file )



