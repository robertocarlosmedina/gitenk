import os
from time import sleep
from pynput.keyboard import Key, Controller

class Auth:
    def __init__(self):
        self.keyboard = Controller()

    def run(self):
        token = "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"
        array = list(token)

        sleep(2)
        for chr in array:
            self.keyboard.press(chr)
            self.keyboard.release(chr)

        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

        for chr in token:
            self.keyboard.press(chr)
            self.keyboard.release(chr)

        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
