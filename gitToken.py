import os
from time import sleep
from pynput.keyboard import Key, Controller
from authThreadHandler import ThreadTask

keyboard = Controller()

# password = input("Auth: ")
password = ""
authPass = ""

class Push:
    def __init__(self):
        pass

    def run(self):
        os.system("git add .")
        os.system("git commit -m 'update'")
        os.system("git push")
        os.system("echo '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'")

class Auth:
    def __init__(self):
        pass

    def run(self):
        os.system("echo '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'")
        keyboard.press(Key.enter)

if (password == authPass):
    array= [Push(), Auth()]

    for item in array:
        th = ThreadTask(item)
        th.start()
    # print("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")

else:
    print("auth: validation error")