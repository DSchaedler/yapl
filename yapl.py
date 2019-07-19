#Yet Another Pack Launcher
#Dee Schaedler

#Let's not lose the source this time

#Imports
import os.path
from os import path
import urllib2

#Check for cmpdl
cmpdl_test = path.exists('cmpdl-1.2.jar')
print("cmpdl present: " + str(cmpdl_test))

#Download cmpdl if missing
if(cmpdl_test == False):
    print("cmpdl missing. Downloading...")

    #Use urllib2 to grab cmpdl
    cmpdl_data = urllib2.urlopen('https://github.com/Vazkii/CMPDL/releases/download/1.2/cmpdl-1.2.jar')
    data_to_write = cmpdl_data.read()

    #write cmpdl file
    with open('cmpdl-1.2.jar', 'wb') as f:
        f.write(data_to_write)

    #re-run cmpdl test
    cmpdl_test = path.exists('cmpdl-1.2.jar')
    print("cmpdl present: " + str(cmpdl_test))
