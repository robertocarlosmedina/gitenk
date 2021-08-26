import os
from time import sleep
from pynput.keyboard import Key, Controller

class Auth:
    def __init__(self):
        self.keyboard = Controller()

    def enterKeyPress(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
    
    def readCredentials(self):
        file_credentials = open("./src/credentials.txt", "r")
        line = file_credentials.readlines()
        return line[0]

    def run(self):
        token = list(self.readCredentials())
        # print(self.readCredentials())

        sleep(3)
        for chr in token:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()

        for chr in token:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()
