import os
from threading import Thread


class ThreadOFTask(Thread):
    def __init__(self, obj):
        Thread.__init__(self)
        self.obj = obj
    
    def run(self):
        self.obj.run()
        
        