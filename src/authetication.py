import os
from time import sleep
from pynput.keyboard import Key, Controller

class Auth:
    def __init__(self):
        self.keyboard = Controller()

    def enterKeyPress(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def run(self):
        token = "ghp_FoaRkSJnDD5ngoFymEtczNDscPjInh41skpZN1"
        array = list(token)

        sleep(3)
        for chr in array:
            self.keyboard.press(chr)
            self.keyboard.release(chr)

        self.enterKeyPress()

        for chr in token:
            self.keyboard.press(chr)
            self.keyboard.release(chr)

        self.enterKeyPress()
