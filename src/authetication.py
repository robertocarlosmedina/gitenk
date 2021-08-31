import os
from time import sleep
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
        # file_credentials.close()
        return line[0]

    def getUseCredentials(self):
        token = self.readCredentials()
        sleep(3)
        for chr in token:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()

        for chr in token:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()

    def showCredentials(self):
        print(f"Github token: {self.readCredentials()}")

    def changeCedentials(self, newToken):
        file_credentials = open("/usr/bin/credentials.txt", "w")
        file_credentials.write(newToken)
        file_credentials.close()

