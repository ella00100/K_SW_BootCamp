#n개의 도시 - 일직선 상
#기름 충전 - 도시마다 주유소 - 가격 다름


from sys import stdin

n = int(stdin.readline())
l = list(map(int,stdin.readline().split()))
p = list(map(int,stdin.readline().split()))

total = 0
min_cost = p[0]

for i in range(n-1):
    if p[i] <= min_cost:
        min_cost = p[i]
    total += min_cost*l[i]

print(total)
