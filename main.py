import os
import sys
from src.taskHandler import ThreadOFTask
from src.action import GitAction
from src.authetication import Auth

# password = input("Auth: ")
password = ""
authPass = ""

if (password == authPass and len(sys.argv)>1):
    path = input("File path: ")
    commitHeader = input("Commit header: ")
    commitDescription = input("Commit description: ")

    objectArray = [GitAction(sys.argv[1], path, commitHeader, commitDescription), Auth()]
    for obj in objectArray:
        th_task = ThreadOFTask(obj)
        th_task.start()
    # os.system("clear")

else:
    print("auth: validation error")