from collections import defaultdict

def dfs(graph, start):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if len(path) == len(graph):
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))

    return []

m = int(input())
for _ in range(m):
    A_addr = input().split()[1:]
    B_addr = input().split()[1:]

    graph = defaultdict(list)
    for i in range(len(A_addr)-1):
        if A_addr[i+1] == A_addr[i]:
            continue
        graph[A_addr[i]].append(A_addr[i+1])
        graph[A_addr[i+1]].append(A_addr[i])

    common_path = []
    for i in range(len(B_addr)-1):
        if B_addr[i+1] == B_addr[i]:
            continue
        path = dfs(graph, B_addr[i])
        if B_addr[i+1] in path:
            common_path.extend(path[path.index(B_addr[i]):path.index(B_addr[i+1])+1])

    common_set = set(common_path)
    common = list(common_set)
    common.sort()

    print(len(common))
