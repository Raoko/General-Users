#DEVELOPER ONLY!
#RUN ON CONSOLE
#    "Python setup.py py2exe"
#without the quotaions
#
from distutils.core import setup
import py2exe
import Files
import subprocess
import time

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

print "\nINSTALLING DRIVER...\n\n"

setup(windows=["Files\install_driver.py"])

#opens driver
#WINDOWS ONLY
sleep = 3
time.sleep(sleep)
subprocess.call(["dist\install_driver.exe"])

print "\nDOWNLOAD COMPLETE!!\n\n\n"
                 


