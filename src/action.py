import os
import stdiomask
from src.authetication import Auth

# Each function of this class is considerate a action to be executed 
# by the package.
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

    def getTokenCredentials(self):
        personal_token = self.auth.getSpecificCredential('token')
        print(f"Personal Token: {personal_token}")
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
