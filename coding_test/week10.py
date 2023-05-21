from sys import stdin

n = int(input())
n_list = list(map(int, stdin.readline().split()))

ase_start = n_list[0]
ase_end = n_list[0]
hight = []

for i in range(1,n):
    if n_list[i] <= ase_end: #내리막길 일 때 둘 다 옆으로
        ase_start = n_list[i]
        ase_end = n_list[i]
    else: #오르막길 일 때 end값만 뒤로
        ase_end = n_list[i]
    h = ase_end - ase_start
    hight.append(h)

print(max(hight))