from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
import subprocess
import time
from appJar import gui
import sys

class webmate():

    def __init__(self, URL=None):
        self.URL = URL

    def loadDriver(self, PHANTOM=False):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("--disable-popup-blocking")
        if PHANTOM == True:
            self.chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.get(self.URL)

    def formInput(self, ID=None, XPATH=None, NAME=None, KEY=None, pressEnter=False):
        time.sleep(0.1)
        self.driver.implicitly_wait(10)
        if XPATH:
            elem = self.driver.find_element_by_xpath(XPATH)
        elif ID:
            elem = self.driver.find_element_by_id(ID)
        elif NAME:
            elem = self.driver.find_element_by_name(NAME)
        elem.send_keys(KEY)
        if pressEnter == True:
            time.sleep(1)
            elem.send_keys(Keys.RETURN)

    def buttonClick(self, ID=None, XPATH=None, NAME=None):
        time.sleep(0.1)
        self.driver.implicitly_wait(10)
        if XPATH:
            self.driver.find_element_by_xpath(XPATH).click()
        elif ID:
            self.driver.find_element_by_id(ID).click()
        elif NAME:
            self.driver.find_element_by_name(NAME).click()

    def kill(self, arg, times=1):
        for i in range(times):
            subprocess.call(["taskkill", "/f", "/IM", arg])

class loginbox():

    def __init__(self, title=None, color1=None, color2=None, font=None, header=None, username=None, password=None):
        self.title = title
        self.color1 = color1
        self.color2 = color2
        self.font = font
        self.header = header
        self.username = username
        self.password = password
        self.login = None


    def frame(self):
        # create a GUI variable called app
        self.app = gui(self.title, "300x180")
        self.app.setBg(self.color1)
        self.app.setFont(self.font)
        # add & configure widgets - widgets get a name, to help referencing them later
        self.app.addLabel("title", self.header)
        self.app.setLabelBg("title", self.color2)

        self.app.addLabelEntry("Username")
        self.app.addLabelSecretEntry("Password")
        self.app.setFocus("Username")
        # link the buttons to the function called press
        self.app.addButtons(["Submit", "Cancel"], self.press)
        self.but = self.app.button

    def start(self):
        self.app.go()

    def press(self, but):
        if but == "Cancel":
            self.login = "close"
            self.app.stop()
        else:
            usr = self.app.getEntry("Username")
            pwd = self.app.getEntry("Password")
            if usr == self.username:
                if pwd == self.password:
                    self.login = True
                    self.app.stop()
                else:
                    pass
            else:
                pass

if __name__ == "__main__":
    pass
