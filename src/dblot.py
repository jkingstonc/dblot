from db.connection import *
import time

class _DBlot: 
    def __init__(self, func, db=""):
        self.connection = connect(db)
        self.cursor = self.connection.cursor()
        self.function = func
  
    def __call__(self, *args, **kwargs):
        t1 = time.time()

        self.cursor.execute(kwargs['execute'])
        for row in self.cursor.fetchall():
            self.function(row=row)

        #result = self.function(*args, **kwargs) 
        print("function took {}".format(time.time()-t1))
        return True
        self.connection.close()

# wrap _Cache to allow for deferred calling
def DBlot(function=None, db=""):
    if function:
        return _DBlot(function)
    else:
        def wrapper(function):
            return _DBlot(function, db)
        return wrapper