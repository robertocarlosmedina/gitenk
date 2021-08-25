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
        # os.system("echo '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'")

class Auth:
    def __init__(self):
        pass

    def run(self):
        # os.system("echo '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'")
        token = "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"
        array = list(token)
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

        # sleep(2)

        # keyboard.press('_')
        # keyboard.release('_')
        # sleep(2)
        # keyboard.press('0')
        # keyboard.release('0')

if (password == authPass):
    array= [Push(), Auth()]

    for item in array:
        th = ThreadTask(item)
        th.start()
    # print("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")

else:
    print("auth: validation error")