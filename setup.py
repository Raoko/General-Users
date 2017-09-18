# setup.py
from distutils.core import setup
import py2exe
import Files
import os

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



