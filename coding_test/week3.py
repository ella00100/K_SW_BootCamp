from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6) #재귀 깊이 제한 풀기

def dfs(node):
    visited[node] = 1
    for child in graph[node]:
        if not visited[child]:
            parent[child] = node
            dfs(child)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
parent = [0] * (n+1)

for i in range(n-1):
        a, b = map(int, stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
        i += 1
for i in range(n+1):
    graph[i].sort()

dfs(1)

parent.pop(0)
parent.pop(0)
print(*parent, sep='\n')