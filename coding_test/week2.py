from sys import stdin

n = int(input())
count = 0
stack = []

for _ in range(n):
    stat = stdin.readline().strip()
    stack.append(stat[0])
    for c in stat[1:]:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        count += 1
    stack = []

print(count)