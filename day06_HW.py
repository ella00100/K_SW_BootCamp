# prob 9.2

def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

count = 0
for i in get_odds():
    count += 1
    if count == 3:
        print(i)