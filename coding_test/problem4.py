import heapq
from sys import stdin

def find_hp(start, graph):
    distance = [INF] * (n * m)
    distance[start] = graph[0][0]
    q = []
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        x, y = now // m, now % m

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            next_node = nx * m + ny
            cost = dist + graph[nx][ny]

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance[n * m - 1]


INF = int(1e9)

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    n = int(input())
    m = n

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().strip().split())))

    print(find_hp(0, graph))

