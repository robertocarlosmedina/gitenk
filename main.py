import os
from time import sleep
from pynput.keyboard import Key, Controller
from src.authThreadHandler import ThreadTask

keyboard = Controller()

# password = input("Auth: ")
password = ""
authPass = ""

class GitAction:
    def __init__(self):
        pass

    def run(self):
        os.system("git add .")
        os.system("git commit -m 'update'")
        os.system("git push")
        # print(s)
        # os.system("clear")

class Auth:
    def __init__(self):
        pass

    def run(self):

        token = "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"
        array = list(token[3:-29])
        # array = list(token)

        sleep(2)
        for chr in array:
            keyboard.press(chr)
            keyboard.release(chr)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        for chr in token:
            keyboard.press(chr)
            keyboard.release(chr)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

if (password == authPass):
    array= [GitAction(), Auth()]

    for item in array:
        th = ThreadTask(item)
        th.start()
    # os.system("clear")

else:
    print("auth: validation error")