n = int(input())

pre = []
for i in range(n):
    p = input().split()
    pre.append((p[0], p[-1]))

for i in range(n):
    for j in range(n):
        if pre[i][1] == pre[j][0]:
            pre.append((pre[i][0], pre[j][1]))

m = int(input())
que = []

for i in range(m):
    q = input().split()
    que.append((q[0], q[-1]))

for i in range(m):
    result = False
    for j in pre:
        if que[i] == j:
            result = True
            break
    print('T' if result else 'F')
