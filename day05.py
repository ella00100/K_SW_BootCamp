#closures

def calculate():
    x=1
    y=2

    def add_sub(n):
        return x + n + y

    return add_sub

c1 = calculate()
for i in range(5):
    print(c1(i))

def calculate2():
    x=1
    y=2
    def add_sub(n):
        nonlocal x
        x = 11
        return x + n - y
    return add_sub

c2 = calculate2()
for i in range(5):
    print(c2(i))
