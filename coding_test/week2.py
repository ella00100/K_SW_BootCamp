import sys
sys.setrecursionlimit(10**6)

n,m = map(int, sys.stdin.readline().rstrip().split())

node = [[] for _ in range(n+1)]
sangsa_num = list(map(int, sys.stdin.readline().rstrip().split()))
cing = [0 for _ in range(n + 1)]

for i in range(1, n+1):
    if sangsa_num[i - 1] != -1:
        node[sangsa_num[i - 1]].append(i)

for j in range(m):
    num, w = map(int, sys.stdin.readline().rstrip().split())
    cing[num] += w

stack = [1]
while stack:
    curr = stack.pop()
    for k in node[curr]:
        cing[k] += cing[curr]
        stack.append(k)

cing = cing[1:]
for i in cing:
    print(i, end=" ")