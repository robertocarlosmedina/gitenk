import os
import sys
import stdiomask
from time import sleep
from pynput.keyboard import Key, Controller
from threading import Thread

# This class will allow to executed threads for a multiple number of function 
class FunctionThreadTask(Thread):
    def __init__(self, function_sent):
        Thread.__init__(self)
        self.function_toExec = function_sent

    def run(self):
        self.function_toExec()

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
        file_credentials.close()
        return line

    def getUseCredentials(self):
        user_credentials = self.readCredentials()
        sleep(5)
        for chr in user_credentials[0]:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()

        for chr in user_credentials[1]:
            self.keyboard.press(chr)
            self.keyboard.release(chr)
        self.enterKeyPress()
    
    def getSpecificCredential(self, credentialsName):
        if(credentialsName == "token"):
            return self.readCredentials()[1]
        elif(credentialsName == "username"):
            return self.readCredentials()[0]

    def showCredentials(self):
        print(f"Github username: {self.readCredentials()[0][0:-1]}")
        print(f"Github token: {self.readCredentials()[1]}")
        input("\nClick enter to close.")
        os.system("clear")

    def changeCedentials(self,newUserName=None,newToken=None):
        if(newToken and newUserName):
            file_credentials = open("/usr/bin/credentials.txt", "w")
            file_credentials.write(f"{newUserName}\n{newToken}")
            file_credentials.close()
        elif(newToken != None):
            username = self.readCredentials()[0]
            file_credentials = open("/usr/bin/credentials.txt", "w")
            print(newToken)
            file_credentials.write(f"{username[0:-1]}")
            file_credentials.write("\n")
            file_credentials.write(f"{newToken}")
            file_credentials.close()
        else:
            token = self.readCredentials()[1]
            file_credentials = open("/usr/bin/credentials.txt", "w")
            file_credentials.write(f"{newUserName}")
            file_credentials.write("\n")
            file_credentials.write(f"{token}")
            file_credentials.close()

# Each function of this class is considerate a action to be executed 
# by the package.
class GitAction:
    def __init__(self):
        self.auth = Auth()
        self.path = None
        self.commitHeader = None
        self.commitMessage = None
        self.forcePush = False
    
    def setForce(self):
        self.forcePush = True
    
    def unsetForce(self):
        self.forcePush = False
    
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
        return True

    def push(self):        
        os.system(f"git add {self.path}")
        if (self.commitHeader and self.commitMessage):
            os.system(f"git commit -m '{self.commitHeader}' -m '{self.commitMessage}'")
        elif(self.commitHeader == None):
            os.system(f"git commit -m '{self.commitMessage}'")
        else:
            os.system(f"git commit -m '{self.commitHeader}'")

        if(self.forcePush):
            os.system("git push --force")
        else:
            os.system("git push")       
        return True

    def pull(self):
        os.system("git pull")
    
    def showCredentials(self):
        self.auth.showCredentials()
        return True

    def getTokenCredentials(self):
        personal_token = self.auth.getSpecificCredential('token')
        print(f"Personal Token: {personal_token}")
        input("\nClick enter to close.")
        os.system("clear")
        return True
    
    def getUserNameCredentials(self):
        username = self.auth.getSpecificCredential('username')
        print(f"Username: {username[0:-1]}")
        return True
    
    def changeCredentials(self):
        newUserName = input("New username: ")
        newToken = stdiomask.getpass(prompt='New Token: ', mask='*')
        if(newToken!= "" and newUserName != ""):
            self.auth.changeCedentials(newUserName=newUserName,newToken=newToken)
            return True
        return False

    def tokenCredentialChange(self):
        newToken = stdiomask.getpass(prompt='New Token: ', mask='*')
        if(newToken != ""):
            if("\n" in newToken):
                self.auth.changeCedentials(newToken=newToken.split("\n")[0])
            else:
                self.auth.changeCedentials(newToken=newToken)
            return True
        return False
    
    def usernameCredentialChange(self):
        newUserName = input("New username: ")
        if (newUserName != ""):
            if("\n" in newUserName):
                self.auth.changeCedentials(newUserName=newUserName.split("\n")[0])
            else:
                self.auth.changeCedentials(newUserName=newUserName)
            return True
        return False


gitAction = GitAction()
# List of the possible commands for the package and their possible
# subcommands that can be used
cmds_dict = {\
    "push":[[gitAction.push, gitAction.authentication],\
        {\
        "-force":[gitAction.setForce]\
        }],\
    "pull":[[gitAction.pull, gitAction.authentication]],\
    "show":[[gitAction.showCredentials],\
        {\
        "token":[gitAction.getTokenCredentials],\
        "username":[gitAction.getUserNameCredentials]\
        }],\
    "change":[[gitAction.changeCredentials], 
        {\
        "token":[gitAction.tokenCredentialChange],\
        "username":[gitAction.usernameCredentialChange]
        }]
    }
    
validOperation = False
validCommitInputValues = False
secunSubCommandsUsed = False
pushAndPullAction = False

if (len(sys.argv)>1):
    for cmd, cmd_related_actions in cmds_dict.items():
        cmd_actions = cmd_related_actions[0]
        if(sys.argv[1]==cmd):
            # Check if it was the push sub commands passed in the sub parameter
            # to set the commit values and path to them
            if (cmd == "push"):
                validCommitInputValues = gitAction.setUPCommitValues()
    
            # if there is a subcommand sent this will run in the the cmdsub dict
            # that are in the commad subcommands
            if((len(sys.argv)==3)and(cmd != "push")and(cmd!="pull")):
                if(len(cmd_related_actions)>1):
                    subCommands = cmd_related_actions[1]
                    for subcmd,subCommand_actions in subCommands.items():
                        if(sys.argv[2] == subcmd):
                            validOperation = subCommand_actions[0]()
                            secunSubCommandsUsed = True
                            validOperation = True
                    if(not secunSubCommandsUsed):
                        validOperation = False

            # if it is a valid operation and all the commit values are correctly set up
            # the function related to the command start the execution, and if there is more than
            # one function related to the command, eacth of them are executed in a thread.
            if ((validCommitInputValues and (cmd == "push"))or(cmd == "pull")):
                # check if it any sub commands bo execute them  first
                if(len(sys.argv)==3):
                    for subCmd, action in cmd_related_actions[1].items():
                        if(sys.argv[2]==subCmd):
                            action[0]()
                # Running throug the actions and execute them by threads
                if(len(cmd_actions)>1):
                    for act in cmd_actions:
                        th_task = FunctionThreadTask(act)
                        th_task.start()
                    validOperation = True
                else:
                    validOperation = action[0]()
                pushAndPullAction = True
            
            if((len(sys.argv)<3) and not pushAndPullAction):
                for action in cmd_actions:
                    validOperation = action()

if(not validOperation):
    print("gitenk error: command error.")