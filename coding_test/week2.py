from sys import stdin

n, k = map(int, stdin.readline().split())
num = list(range(1, n+1))
i = 0
result = []

while num:
    i = (i + k - 1) % len(num)
    result.append(num.pop(i))

print('<' + ', '.join(map(str, result)) + '>')