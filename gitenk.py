import os
import sys
from time import sleep
from pynput.keyboard import Key, Controller
from threading import Thread


class ThreadOFTask(Thread):
    def __init__(self, obj):
        Thread.__init__(self)
        self.obj = obj
    
    def run(self):
        self.obj.run()

class ThreadOSTask(Thread):
    def __init__(self, cmd):
        Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        print(self.cmd)
        os.system(self.cmd)

class Auth:
    def __init__(self):
        self.keyboard = Controller()

    def enterKeyPress(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
    
    def readCredentials(self):
        file_credentials = open("credentials.txt", "r")
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

class GitAction:
    def __init__(self, action, path=None, commitHeader=None, commitMessage=None):
        self.action = action
        self.filePath = path
        self.commitHeader = commitHeader
        self.commitMessage = commitMessage

    def run(self, ):
        if (self.action == "push"):
            os.system(f"git add {self.filePath}")
            if (self.commitHeader != None):
                os.system(f"git commit -m '{self.commitHeader}' -m '{self.commitMessage}'")
            else:
                os.system(f"git commit -m '{self.commitMessage}'")
            os.system("git push")
        
        elif(self.action == "pull"):
            os.system("git pull")

        # os.system("clear")

if (len(sys.argv)>1):
    if(sys.argv[1]=="push"):
        path = input("File path: ")
        commitHeader = input("Commit header: ")
        commitDescription = input("Commit description: ")
        objectArray = [GitAction(sys.argv[1], path, commitHeader, commitDescription), Auth()]
    else:
        objectArray = [GitAction(sys.argv[1]), Auth()]
    for obj in objectArray:
        th_task = ThreadOFTask(obj)
        th_task.start()
    # os.system("clear")

else:
    print("Invalid command")
