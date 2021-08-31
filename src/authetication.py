import os
from time import sleep
import getpass
from pynput.keyboard import Key, Controller

# This class has the main goal the care about all the Authentication and 
# security question, for a better exeperience to the user.
class Auth:
    def __init__(self):
        self.keyboard = Controller()

    def enterKeyPress(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
    
    def readCredentials(self):
        file_credentials = open("/usr/bin/credentials.txt", "r")
        line = file_credentials.readlines()
        file_credentials.close()
        return line

    def getUseCredentials(self):
        user_credentials = self.readCredentials()
        sleep(3)
        for chr in user_credentials[0]:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()

        for chr in user_credentials[1]:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()
    
    def getSpecificCredential(self, credentialsName):
        if(credentialsName == "token"):
            return self.readCredentials()[1]
        elif(credentialsName == "username"):
            return self.readCredentials()[0]

    def showCredentials(self):
        print(f"Github username: {self.readCredentials()[0][0:-1]}")
        print(f"Github token: {self.readCredentials()[1]}")
        input("\nClick enter to close.")
        os.system("clear")

    def changeCedentials(self,newUserName=None,newToken=None):
        if(newToken and newUserName):
            file_credentials = open("/usr/bin/credentials.txt", "w")
            file_credentials.write(f"{newUserName}\n{newToken}")
            file_credentials.close()
        elif(newToken != None):
            username = self.readCredentials()[0]
            file_credentials = open("/usr/bin/credentials.txt", "w")
            print(newToken)
            file_credentials.write(f"{username[0:-1]}")
            file_credentials.write("\n")
            file_credentials.write(f"{newToken}")
            file_credentials.close()
        else:
            token = self.readCredentials()[1]
            file_credentials = open("/usr/bin/credentials.txt", "w")
            file_credentials.write(f"{newUserName}")
            file_credentials.write("\n")
            file_credentials.write(f"{token}")
            file_credentials.close()
