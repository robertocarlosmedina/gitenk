import os
from threading import Thread


class ThreadOFTask(Thread):
    def __init__(self, function_sent):
        Thread.__init__(self)
        self.function_toExec = function_sent
    
    def run(self):
        self.function_toExec()
        
        