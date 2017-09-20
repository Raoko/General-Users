from Webmate import webmate
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
        self.user()
        self.main()

    def user(self):
        self.users = [
                    "general1",
                    "general2",
                    "general3"
                        ]
        self.usuario = pg.prompt(text="Username", title="Consumer Law Group")
        if self.usuario in self.users:
            for i in range(1):
                contrasena = pg.password(text="Password", title="Consumer Law Group")
                if contrasena == "consumer123":
                    break
                else:
                    x = pg.confirm(text="Wrong Username/Password", title="Consumer Law Group", buttons=["Try again", "Quit"])
                    if x == "Try again":
                        self.user()
                    else:
                        sys.exit()
                    
        else:
            y = pg.confirm(text="Would you like to quit application or try again?", title="Consumer Law Group", buttons=["Try again", "Quit"])
            if y == "Try again":
                self.user()
            else:
                sys.exit()
                
              
    def main(self):
        while True:
            sleep = 0.1 #seconds of sleep
            self.startButton = pg.confirm(text='\n\n\nCLG USER:     ' + self.usuario + '\n\n', title='Consumer Law Group',buttons=['\n    Office    \n', '\nPhone System\n', '\n     Logic     \n', '\nEmail(Correo)\n'])
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
        self.officelogin.formInput(XPATH='//*[@id="edit-name"]', KEY=self.usuario)
        self.officelogin.formInput(XPATH='//*[@id="edit-pass"]', KEY='clg1234!')
        self.officelogin.buttonClick(XPATH='//*[@id="edit-submit"]')
        self.glob.kill('chromedriver.exe')

    def phone(self):
        self.phonesystemlogin = webmate('http://agents.phonesystem.yourclg.com/agents/')
        self.phonesystemlogin.loadDriver(PHANTOM=False)
        self.phonesystemlogin.formInput(XPATH='//*[@id="username"]', KEY=self.usuario)
        self.phonesystemlogin.formInput(XPATH='//*[@id="password"]', KEY='clg1234!')
        self.phonesystemlogin.buttonClick(XPATH='//*[@id="loginButton"]')
        self.glob.kill('chromedriver.exe')

    def logic(self):
        self.logiclogin = webmate('https://clg.irslogics.com/')
        self.logiclogin.loadDriver(PHANTOM=False)
        self.logiclogin.formInput(XPATH='//*[@id="txtUsername2"]', KEY=self.usuario + "@consumerlaw.com")
        self.logiclogin.formInput(XPATH='//*[@id="txtPassword2"]', KEY='Santana007!')
        self.logiclogin.buttonClick(XPATH='//*[@id="btnLogin2"]')
        self.glob.kill('chromedriver.exe')

    def email(self):
        self.emaillogin = webmate('https://goo.gl/qixfyG')
        self.emaillogin.loadDriver(PHANTOM='False')
        self.emaillogin.formInput(XPATH='//*[@id="cred_userid_inputtext"]', KEY=self.usuario + "@consumerlaw.com")
        self.emaillogin.formInput(XPATH='//*[@id="cred_password_inputtext"]', KEY='Santana007!', pressEnter=True)
        self.glob.kill('chromedriver.exe')

if __name__ == '__main__':
    log = automatelogin()

