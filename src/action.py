import os

class GitAction:
    def __init__(self):
        pass

    def run(self):
        os.system("git add .")
        os.system("git commit -m 'update'")
        os.system("git push")
        # print(s)
        # os.system("clear")