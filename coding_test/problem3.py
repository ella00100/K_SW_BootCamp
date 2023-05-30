from sys import stdin

def bfs(start, end, graph):
    visited = set([start])
    queue = [start]
    count = 0
    found = False
    while queue and not found:
        count += 1
        for _ in range(len(queue)):
            x = queue.pop(0)
            for y in graph[x]:
                if y not in visited:
                    visited.add(y)
                    queue.append(y)
                    if y == end:
                        found = True
                        break
        if found:
            break
    if found:
        return count
    else:
        return "No"


m = int(input())
results = []
for _ in range(m):
    n = int(input())
    friend = {i: set() for i in range(1, n+1)}
    for _ in range(n):
        sns = list(map(int, stdin.readline().split()))
        i = sns[0]
        f = sns[1:]
        for j in f:
            friend[i].add(j)
            friend[j].add(i)
    a, b = map(int, input().split())
    result = bfs(a, b, friend)
    results.append(result)

for i in range(len(results)):
    print(results[i])