import os
import sys
from src.taskHandler import FunctionThreadTask
from src.action import GitAction

gitAction = GitAction()
# List of the possible commands for the package
cmds_dict = {"push":[gitAction.push, gitAction.authentication], "pull":[gitAction.pull, gitAction.authentication], "show":[gitAction.showCredentials],\
     "change":[gitAction.changeCredentials]}

if (len(sys.argv)>1):
    validOperation = True
    for cmd, actions in cmds_dict.items():
        if(sys.argv[1]==cmd):
            # check if it was the push sub commands passed in the sub parameter
            # to set the commit values and path to them
            if (cmd == "push"):
                validOperation = gitAction.setUPCommitValues()

            # if it is a valid operation and all the commit values are correctly set up
            # the function related to the command start the execution, and if there is more than
            # one function related to the command, eacth of them are executed in a thread.
            if validOperation:
                if(len(actions)>1):
                    for act in actions:
                        th_task = FunctionThreadTask(act)
                        th_task.start()
                else:
                    actions[0]()
            else:
                print("\nAction Error: try it again.")