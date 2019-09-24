import dblot

@dblot.DBlot(db="test.db")
def test(*args, **kwargs): 
    if kwargs['row'][0] == 2:
        return 1
    return 0

if __name__ == "__main__":
    print(sum(test(execute="SELECT * FROM t;")))