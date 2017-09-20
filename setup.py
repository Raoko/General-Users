#DEVELOPER ONLY!
#PY2EXE ""pip install http://sourceforge.net/projects/py2exe/files/latest/download?source=files""
#RUN ON CONSOLE
#
#    "Python setup.py py2exe"
#
#without the quotaions
#Sorry for the messy script

from distutils.core import setup
import py2exe
import Files
import subprocess
import time
#Start
print "\n\n     1.) COMPILING FILES...\n\n"
time.sleep(2)
print "     Please dont close console\n\n"
time.sleep(3)
wd_path = 'C:\\Python27\\Lib\\site-packages\\selenium\\webdriver'
required_data_files = [('selenium/webdriver/remote',['{}\\remote\\getAttribute.js'.format(wd_path),'{}\\remote\\isDisplayed.js'.format(wd_path)])]

setup(
    windows=[
        {
"script": "Files/login.py",
"icon_resources": [(1,"Files\user.ico")],
        }],
             data_files = required_data_files,
              options={
                  'py2exe':{
                      'packages': ['selenium', 'Webmate', 'pyautogui'],
                      "skip_archive":True,
                      "unbuffered": True,
                      "optimize":2
              }
          }
      )

time.sleep(1)
print "\n       2.) INSTALLING DRIVER...\n\n"
time.sleep(2)
setup(windows=["Files\install_driver.py"])
#opens driver
#WINDOWS ONLY
sleep = 3
print "\n       3.) UNZIPPING FILES...\n"
time.sleep(sleep)
subprocess.call(["dist\install_driver.exe"])
time.sleep(1)
print "\n       DOWNLOAD COMPLETE!!!\n\n"
time.sleep(1)
#Done
                 


