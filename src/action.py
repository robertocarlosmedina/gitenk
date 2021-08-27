import os
from src.authetication import Auth

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

        # os.system("clear")