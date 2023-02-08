sum_value = 0
for n in range(10,0,-1):
    sum_value += n
print(sum_value)

def Addnum(num):
    if num <= 1:
        return 1
    return num + Addnum(num-1)
print(Addnum(10))