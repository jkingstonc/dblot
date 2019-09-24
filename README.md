# dblot
A lightweight database analysis library for Python3

'''
import dblot

@dblot.analyser(db="test.db")
def test(*args, **kwargs): 
    if kwargs['row'][0] == 2:
        return 1
    return 0

if __name__ == "__main__":
    print("{} rows with id of 2".format(sum(test(execute="SELECT * FROM t;"))))
'''
