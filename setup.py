# setup.py
from distutils.core import setup
import py2exe

setup(windows=["login.py", "install_driver"],
      options={
          'py2exe':{
              'packages': ['selenium', 'Webmate', 'pyautogui'],
              "skip_archive":True,
              "unbuffered": True,
              "optimize":2
              }
          }
      )
