#3
#336
#222
#625

from sys import stdin

n = int(stdin.readline())
dice = [[] for _ in range(n)]
price = []

for i in range(n):
    dice[i] = list(map(int, stdin.readline().split()))
    if dice[i][0] == dice[i][1] == dice[i][2]:
        price.append(10000+ dice[i][0]*1000)
    elif dice[i][0] == dice[i][1] or dice[i][1] == dice[i][2] or dice[i][2] == dice[i][0]:
        price.append(1000 + max(dice[i])*100)
    else:
        price.append(max(dice[i])*100)

print(max(price))


