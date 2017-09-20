# setup.py
#DEVELOPER ONLY
from distutils.core import setup
import py2exe
import Files
import subprocess
import time

wd_path = 'C:\\Python27\\Lib\\site-packages\\selenium\\webdriver'
required_data_files = [('selenium/webdriver/remote',['{}\\remote\\getAttribute.js'.format(wd_path),'{}\\remote\\isDisplayed.js'.format(wd_path)])]

setup(
    windows=["Files\login.py", "Files\install_driver.py"],
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

#opens driver
#WINDOWS ONLY
sleep = 3
time.sleep(sleep)
subprocess.call(["dist\install_driver.exe"])
                 


