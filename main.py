import os
import sys
from src.taskHandler import FunctionThreadTask
from src.action import GitAction



gitAction = GitAction()
cmds_dict = {"push":[gitAction.push, gitAction.authentication], "pull":[gitAction.pull, gitAction.authentication], "show":[gitAction.showCredentials],\
     "change":[gitAction.changeCredentials]}

if (len(sys.argv)>1):
    for cmd, actions in cmds_dict.items():
        if(sys.argv[1]==cmd):
            if(len(actions)>1):
                for act in actions:
                    th_task = FunctionThreadTask(act)
                    th_task.start()
            else:
                actions[0]()
else:
    print("Invalid command")