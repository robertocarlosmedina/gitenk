import os
from src.authetication import Auth

class GitAction:
    def __init__(self):
        self.auth = Auth()
        self.path = None
        self.commitHeader = None
        self.commitMessage = None
    
    def setUPCommitValues(self):
        self.path = input("File path: ")
        self.commitHeader = input("Commit header: ")
        self.commitMessage = input("Commit description: ")
    
    def authentication(self):
        self.auth.getUseCredentials()

    def push(self):        
        os.system(f"git add {self.path}")
        if (self.commitHeader != None):
            os.system(f"git commit -m '{self.commitHeader}' -m '{self.commitMessage}'")
        else:
            os.system(f"git commit -m '{self.commitMessage}'")
        os.system("git push")

    def pull(self):
        os.system("git pull")
    
    def showCredentials(self):
        self.auth.showCredentials()
    
    def changeCredentials(self):
        newToken = input("New Token: ")
        self.auth.changeCedentials(newToken)

        # os.system("clear")