#1-6방배정
#남남/여여, 같은 학년
#한방 최대인원 k
#최소 방의 개수를 구해라

from sys import stdin

n, k = map(int,stdin.readline().split())
group= [[0]*2 for _ in range(6)]

for i in range(n):
    s,g = map(int,stdin.readline().split())
    group[g-1][s-1] += 1
    i += 1

room = 0
for i in range(6):
    for j in range(2):
        if group[i][j]%k == 0:
            room += group[i][j]//k
        else:
            room += (group[i][j]//k)+1

print(room)

