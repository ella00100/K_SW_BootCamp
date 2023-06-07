from sys import stdin

n, m = map(int, stdin.readline().split())
Arr = []
for i in range(n):
    col = list(map(int, stdin.readline().split()))
    Arr.append(col)

Arr2 = []
result = []

for i in range(n):
    col2 = list(map(int, stdin.readline().split()))
    Arr2.append(col2)

for i in range(n):
    row = []
    for j in range(m):
        n = Arr[i][j]+Arr2[i][j]
        row.append(n)
    result.append(row)

for n in result:
    output = ' '.join(map(str, n))
    print(output)