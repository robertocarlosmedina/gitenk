import os
import sys
from time import sleep
from pynput.keyboard import Key, Controller
from threading import Thread


class FunctionThreadTask(Thread):
    def __init__(self, function_sent):
        Thread.__init__(self)
        self.function_toExec = function_sent
    
    def run(self):
        self.function_toExec()
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


class GitAction:
    def __init__(self):
        self.auth = Auth()
        self.path = None
        self.commitHeader = None
        self.commitMessage = None
    
    def setUPCommitValues(self):
        self.path = input("File path: ")
        if (self.path == ""):
            self.path == "."

        self.commitHeader = input("Commit header: ")
        if (self.commitHeader == ""):
            self.commitHeader = None

        self.commitMessage = input("Commit description: ")
        if (self.commitMessage == ""):
            self.commitMessage = None

        if(self.commitHeader == None and self.commitMessage == None):
            return False

        return True
    
    def authentication(self):
        self.auth.getUseCredentials()

    def push(self):        
        os.system(f"git add {self.path}")
        if (self.commitHeader != None and self.commitMessage != None):
            os.system(f"git commit -m '{self.commitHeader}' -m '{self.commitMessage}'")
        elif(self.commitHeader == None):
            os.system(f"git commit -m '{self.commitMessage}'")
        else:
            os.system(f"git commit -m '{self.commitHeader}'")

        os.system("git push")

    def pull(self):
        os.system("git pull")
    
    def showCredentials(self):
        self.auth.showCredentials()
    
    def changeCredentials(self):
        newToken = input("New Token: ")
        self.auth.changeCedentials(newToken)

        # os.system("clear")

gitAction = GitAction()
cmds_dict = {"push":[gitAction.push, gitAction.authentication], "pull":[gitAction.pull, gitAction.authentication], "show":[gitAction.showCredentials],\
     "change":[gitAction.changeCredentials]}

if (len(sys.argv)>1):
    validOperation = True
    for cmd, actions in cmds_dict.items():
        if(sys.argv[1]==cmd):

            if (cmd == "push"):
                validOperation = gitAction.setUPCommitValues()

            if validOperation:
                if(len(actions)>1):
                    for act in actions:
                        th_task = FunctionThreadTask(act)
                        th_task.start()
                else:
                    actions[0]()
            else:
                print("\nAction Error: try it again.")
