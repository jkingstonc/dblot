from db.connection import *
import time

class _DBlot: 
    def __init__(self, func, db="", setup=[]):
        self.connection = connect(db)
        self.cursor = self.connection.cursor()
        self.function = func
        for command in setup:
            self.cursor.execute(command)
  
    def __call__(self, *args, **kwargs):
        t1 = time.time()

        self.cursor.execute("""
            SELECT * FROM t;
        """)
        for row in self.cursor.fetchall():
            self.function(row)

        #result = self.function(*args, **kwargs) 
        print("function took {}".format(time.time()-t1))
        return True
        self.connection.close()

# wrap _Cache to allow for deferred calling
def DBlot(function=None, db="", setup=[]):
    if function:
        return _DBlot(function)
    else:
        def wrapper(function):
            return _DBlot(function, db, setup)

        return wrapper


@DBlot(db="test.db", setup=[
    "CREATE TABLE IF NOT EXISTS t (id INT);",
    "INSERT INTO t (id) VALUES (1);",
    "INSERT INTO t (id) VALUES (2);",
    ])
def test(row=""): 
    if row[0] == 2:
        print("found id 2!")

test()
