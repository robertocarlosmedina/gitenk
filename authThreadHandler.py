import os
from threading import Thread
from pynput import keyboard


class ThreadTask(Thread):
    def __init__(self, obj):
        Thread.__init__(self)
        self.obj = obj

    
    def run(self):
        self.obj.run()
        
        