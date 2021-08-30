import os
import sys
from time import sleep
from pynput.keyboard import Key, Controller
from threading import Thread


class ThreadOFTask(Thread):
    def __init__(self, function_sent):
        Thread.__init__(self)
        self.function_toExec = function_sent
    
    def run(self):
        self.function_toExec()

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
        file_credentials = open("/usr/bin/credentials.txt", "r")
        line = file_credentials.readlines()
        file_credentials.close()
        return line[0]

    def getUseCredentials(self):
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

    def showCredentials(self):
        print(f"Github token: {self.readCredentials()}")

    def changeCedentials(self, newToken):
        file_credentials = open("/usr/bin/credentials.txt", "w")
        file_credentials.write(newToken)
        file_credentials.close()

class GitAction:
    def __init__(self):
        self.auth = Auth()
    
    def authentication(self):
        self.auth.getUseCredentials()

    def push(self):        
        path = input("File path: ")
        commitHeader = input("Commit header: ")
        commitMessage = input("Commit description: ")
        os.system(f"git add {path}")
        if (commitHeader != None):
            os.system(f"git commit -m '{commitHeader}' -m '{commitMessage}'")
        else:
            os.system(f"git commit -m '{commitMessage}'")
        os.system("git push")

    def pull(self):
        os.system("git pull")
    
    def showCredentials(self):
        self.auth.showCredentials()
    
    def changeCredentials(self):
        newToken = input("New Token: ")
        self.auth.changeCedentials(newToken)


gitAction = GitAction()
cmds_dict = {"push":[gitAction.push], "pull":[gitAction.pull, gitAction.authentication], "show":[gitAction.showCredentials],\
     "change":[gitAction.changeCredentials]}

if (len(sys.argv)>1):
    for cmd, actions in cmds_dict.items():
        if(sys.argv[1]==cmd):
            if(len(actions)>1):
                for act in actions:
                    th_task = ThreadOFTask(act)
                    th_task.start()
            else:
                actions[0]()
else:
    print("Invalid command")
