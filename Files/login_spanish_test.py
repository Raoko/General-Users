# -*- coding: utf-8 -*-
from Webmate import webmate
from Webmate_test import loginbox
import pyautogui as pg
import time
import sys


'''
Download the following:
----------------------
Python2.7
selenium (package) #pip isntall selenium
pyautogui (package) #pip install pyautogui
Webmate (package) #https://github.com/Raoko/Webmate.git
Chrome Browser
Chromedriver #https://goo.gl/Bvq8BD
'''

class automatelogin():

    def __init__(self):
        self.glob = webmate()
        self.users = [
                    "general1",
                    "general2",
                    "general3"
                     ]
        print self.users
        self.frm = loginbox(title="CLG Login", color1="grey", color2="white", font=13, header="Consumer Law Group", username=self.users[0] or self.users[1], password='Santana')
        self.frm.frame()
        self.frm.start()
        if self.frm.login == True:
            self.main()
        elif self.frm.login == "close":
            sys.exit()
        else:
            self.frm.start()

    def main(self):
        while True:
            sleep = 0.1 #seconds of sleep
            self.startButton = pg.confirm(text='\n\n\nCLG USUARIO:     ' + self.frm.username + '\n\n', title='Consumer Law Group',buttons=['\n    Office    \n', '\nPhone System\n', '\n     Logic     \n', '\nEmail(Correo)\n'])
            if self.startButton == '\n    Office    \n':
                self.office()
                time.sleep(sleep)
                return self.main()

            elif self.startButton == '\nPhone System\n':
                try:
                    self.phone()
                    time.sleep(sleep)
                    return self.main()
                except:
                    pg.alert(text="error 111", title="Consuemr Law Group")
                    return self.main()

            elif self.startButton == '\n     Logic     \n':
                try:
                    self.logic()
                    time.sleep(sleep)
                    return self.main()
                except:
                    pg.alert(text="error 111", title="Consuemr Law Group")
                    return self.main()

            elif self.startButton == '\nEmail(Correo)\n':
                self.email()
                time.sleep(sleep)
                return self.main()

            else:
                break


    def office(self):
        self.officelogin = webmate("http://office.yourclg.com/")
        self.officelogin.loadDriver(PHANTOM=False)
        self.officelogin.formInput(XPATH='//*[@id="edit-name"]', KEY=self.frm.username)
        self.officelogin.formInput(XPATH='//*[@id="edit-pass"]', KEY='clg1234!')
        self.officelogin.buttonClick(XPATH='//*[@id="edit-submit"]')
        self.glob.kill('chromedriver.exe')

    def phone(self):
        self.phonesystemlogin = webmate('http://agents.phonesystem.yourclg.com/agents/')
        self.phonesystemlogin.loadDriver(PHANTOM=False)
        self.phonesystemlogin.formInput(XPATH='//*[@id="username"]', KEY=self.frm.username)
        self.phonesystemlogin.formInput(XPATH='//*[@id="password"]', KEY='clg1234!')
        self.phonesystemlogin.buttonClick(XPATH='//*[@id="loginButton"]')
        self.glob.kill('chromedriver.exe')

    def logic(self):
        self.logiclogin = webmate('https://clg.irslogics.com/')
        self.logiclogin.loadDriver(PHANTOM=False)
        self.logiclogin.formInput(XPATH='//*[@id="txtUsername2"]', KEY=self.frm.username + "@consumerlaw.com")
        self.logiclogin.formInput(XPATH='//*[@id="txtPassword2"]', KEY='Santana007!')
        self.logiclogin.buttonClick(XPATH='//*[@id="btnLogin2"]')
        self.glob.kill('chromedriver.exe')

    def email(self):
        self.emaillogin = webmate('https://goo.gl/qixfyG')
        self.emaillogin.loadDriver(PHANTOM='False')
        self.emaillogin.formInput(XPATH='//*[@id="cred_userid_inputtext"]', KEY=self.frm.username + "@consumerlaw.com")
        self.emaillogin.formInput(XPATH='//*[@id="cred_password_inputtext"]', KEY='Santana007!', pressEnter=True)
        self.glob.kill('chromedriver.exe')

if __name__ == '__main__':
    log = automatelogin()
