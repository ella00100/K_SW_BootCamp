# prob 9.3

def test(func):
    def new_func(*args):
        print("start",end = '\n')
        result = func(*args)
        print(result)
        print("end", end = '\n')
        return result
    return new_func

@test
def sum(a,b):
    return a + b

sum(3,5)