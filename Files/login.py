from Webmate import webmate
import pyautogui as pg
import time

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
        
    def main(self):
        while True:
            sleep = 0.1 #seconds of sleep
            self.startButton = pg.confirm(text='\n\n\nCONSUMER   LAW   GROUP\n\n', title='CLG USER: GENERAL 1',buttons=['\n    Office    \n', '\nPhone System\n', '\n     Logic     \n', '\nEmail(Correo)\n'])
            if self.startButton == '\n    Office    \n':
                self.office()
                time.sleep(sleep)
                continue
            elif self.startButton == '\nPhone System\n':
                self.phone()
                time.sleep(sleep)
                continue
            elif self.startButton == '\n     Logic     \n':
                self.logic()
                time.sleep(sleep)
                continue
            elif self.startButton == '\nEmail(Correo)\n':
                self.email()
                time.sleep(sleep)
                continue
            else:
                break
            
    def office(self):
        self.glob.kill('chrome.exe')
        self.officelogin = webmate("http://office.yourclg.com/")
        self.officelogin.loadDriver(PHANTOM=False)
        self.officelogin.formInput(XPATH='//*[@id="edit-name"]', KEY='general1')
        self.officelogin.formInput(XPATH='//*[@id="edit-pass"]', KEY='clg1234!')
        self.officelogin.buttonClick(XPATH='//*[@id="edit-submit"]')
        self.glob.kill('chromedriver.exe')

    def phone(self):
        self.glob.kill('chrome.exe')
        self.phonesystemlogin = webmate('http://admin.phonesystem.yourclg.com/cti/')
        self.phonesystemlogin.loadDriver(PHANTOM=False)
        self.phonesystemlogin.formInput(XPATH='//*[@id="username"]', KEY='general1')
        self.phonesystemlogin.formInput(XPATH='//*[@id="password"]', KEY='clg1234!')
        self.phonesystemlogin.buttonClick(XPATH='//*[@id="button"]')
        self.glob.kill('chromedriver.exe')

    def logic(self):
        self.glob.kill('chrome.exe')
        self.logiclogin = webmate('https://clg.irslogics.com/')
        self.logiclogin.loadDriver(PHANTOM=False)
        self.logiclogin.formInput(XPATH='//*[@id="txtUsername2"]', KEY='general1@consumerlaw.com')
        self.logiclogin.formInput(XPATH='//*[@id="txtPassword2"]', KEY='Santana007!')
        self.logiclogin.buttonClick(XPATH='//*[@id="btnLogin2"]')
        self.glob.kill('chromedriver.exe')

    def email(self):
        self.glob.kill('chrome.exe')
        self.emaillogin = webmate('https://goo.gl/qixfyG')
        self.emaillogin.loadDriver(PHANTOM='False')
        self.emaillogin.formInput(XPATH='//*[@id="cred_userid_inputtext"]', KEY='general1@consumerlaw.com')
        self.emaillogin.formInput(XPATH='//*[@id="cred_password_inputtext"]', KEY='Santana007!', pressEnter=True)
        self.glob.kill('chromedriver.exe')

if __name__ == '__main__':
    log = automatelogin()
    log.main()
