import os
import sys
from src.taskHandler import ThreadOFTask
from src.action import GitAction
from src.authetication import Auth


if (len(sys.argv)>1):
    if(sys.argv[1]=="push"):
        path = input("File path: ")
        commitHeader = input("Commit header: ")
        commitDescription = input("Commit description: ")
        objectArray = [GitAction(sys.argv[1], path, commitHeader, commitDescription), Auth()]
    else:
        objectArray = [GitAction(sys.argv[1]), Auth()]
    for obj in objectArray:
        th_task = ThreadOFTask(obj)
        th_task.start()
    # os.system("clear")

else:
    print("Invalid command")