import os

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