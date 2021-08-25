import os
from src.authThreadHandler import ThreadTask
from src.action import GitAction
from src.authetication import Auth

# password = input("Auth: ")
password = ""
authPass = ""

if (password == authPass):
    array= [GitAction(), Auth()]

    for item in array:
        th = ThreadTask(item)
        th.start()
    # os.system("clear")

else:
    print("auth: validation error")