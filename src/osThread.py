import os
from threading import Thread

class ThreadOSTask(Thread):
    def __init__(self, cmd):
        Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        print(self.cmd)
        os.system(self.cmd)