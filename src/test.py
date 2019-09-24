import dblot

@dblot.DBlot(db="test.db", execute="SELECT * FROM t;")
def test(row=""): 
    if row[0] == 2:
        print("found id 2!")

if __name__ == "__main__":
    test()