from connection import *
import time

class _DBlot: 
    def __init__(self, func, db=""):
        self.connection = connect(db)
        self.cursor = self.connection.cursor()
        self.function = func
  
    def __call__(self, *args, **kwargs):
        t1 = time.time()
        print("starting analysis of '{}'...".format(kwargs['execute']))
        self.cursor.execute(kwargs['execute'])
        results = []
        for row in self.cursor.fetchall():
            results.append(self.function(*args, **kwargs, row=row))
        print("finished analysis of '{}', took {} seconds".format(kwargs['execute'], time.time()-t1))
        self.connection.close()
        return results

# wrap _Cache to allow for deferred calling
def DBlot(function=None, db=""):
    if function:
        return _DBlot(function)
    else:
        def wrapper(function):
            return _DBlot(function, db)
        return wrapper