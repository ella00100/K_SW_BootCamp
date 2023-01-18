# prob 9.2

def get_odd():
    return (odd_num for odd_num in range(1,10,2))

count = 0
for i in get_odd():
    count += 1
    if count == 3:
        print(i)