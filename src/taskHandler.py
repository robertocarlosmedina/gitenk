from threading import Thread

# This class will allow to executed threads for a multiple number of function 
class FunctionThreadTask(Thread):
    def __init__(self, function_sent):
        Thread.__init__(self)
        self.function_toExec = function_sent

    def run(self):
        self.function_toExec()
        
        