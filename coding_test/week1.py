#2 3 5
#1
from sys import stdin

position = list(map(int, stdin.readline().split()))
position.sort()

move = 0
while position[0] != position[1]-1 or position[1]+1 != position[2]:
    if position[1]+1 < position[2]:
        position[0] = position[2] - 1
        position.sort()
        move += 1
    if position[0] < position[1]-1:
        position[2] = position[0] + 1
        position.sort()
        move += 1

print(move)

