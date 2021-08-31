import os
import subprocess
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

        output = os.system("git push")
        print("\n\noutput: ")
        print(output)

    def pull(self):
        os.system("git pull")
    
    def showCredentials(self):
        self.auth.showCredentials()
    
    def changeCredentials(self):
        newToken = input("New Token: ")
        self.auth.changeCedentials(newToken)
