import dblot

@dblot.DBlot(db="test.db")
def test(*args, **kwargs): 
    if kwargs['row'] == 2:
        print("found id 2!")

if __name__ == "__main__":
    test(execute="SELECT * FROM t;")