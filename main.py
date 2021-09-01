import os
import sys
from time import sleep
from src.taskHandler import FunctionThreadTask
from src.action import GitAction

gitAction = GitAction()
# List of the possible commands for the package and their possible
# subcommands that can be used
cmds_dict = {\
    "push":[[gitAction.unsetForce, gitAction.push, gitAction.authentication],\
        {\
        "-force":[gitAction.setForce]\
        }],\
    "pull":[[gitAction.pull, gitAction.authentication]],\
    "show":[[gitAction.showCredentials],\
        {\
        "token":[gitAction.getTokenCredentials],\
        "username":[gitAction.getUserNameCredentials]\
        }],\
    "change":[[gitAction.changeCredentials], 
        {\
        "token":[gitAction.tokenCredentialChange],\
        "username":[gitAction.usernameCredentialChange]
        }]
    }
    
validOperation = False
validCommitInputValues = False
secunSubCommandsUsed = False
pushAndPullAction = False

if (len(sys.argv)>1):
    for cmd, cmd_related_actions in cmds_dict.items():
        cmd_actions = cmd_related_actions[0]
        if(sys.argv[1]==cmd):
            # check if it was the push sub commands passed in the sub parameter
            # to set the commit values and path to them
            if (cmd == "push"):
                validCommitInputValues = gitAction.setUPCommitValues()
            # if there is a subcommand sent this will run in the the cmdsub dict
            # that are in the commad subcommands
            if((len(sys.argv)==3)and(cmd != "push")and(cmd!="pull")):
                if(len(cmd_related_actions)>1):
                    subCommands = cmd_related_actions[1]
                    for subcmd,subCommand_actions in subCommands.items():
                        if(sys.argv[2] == subcmd):
                            validOperation = subCommand_actions[0]()
                            secunSubCommandsUsed = True

            # if it is a valid operation and all the commit values are correctly set up
            # the function related to the command start the execution, and if there is more than
            # one function related to the command, eacth of them are executed in a thread.
            if ((validCommitInputValues and (cmd == "push"))or(cmd == "pull")):
                if(len(cmd_related_actions)==2):
                    for subCmd, action in cmd_related_actions[1].items():
                        if(sys.argv[2]==subCmd):
                            action[0]()
                            sleep(2)

                if(len(cmd_actions)>1):
                    for act in cmd_actions:
                        th_task = FunctionThreadTask(act)
                        th_task.start()
                    validOperation = True
                else:
                    validOperation = action[0]()
                pushAndPullAction = True
            
            if(not secunSubCommandsUsed and not pushAndPullAction):
                for action in cmd_actions:
                    validOperation = action()
if(not validOperation):
    print("gitenk error: command error.")
