from sys import stdin

n, m = map(int, stdin.readline().split())
fish_graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    fish_graph[b].append(a)

max_count = 0
treated_fish = []

def dfs(graph, start, visited):
    count = 1
    visited[start] = True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)

    return count

for i in range(1, n+1):
    visited = [False] * (n+1)
    count = dfs(fish_graph, i , visited)

    if count > max_count:
        max_count = count
        treated_fish = [i]
    elif count == max_count:
        treated_fish.append(i)
print(*treated_fish)