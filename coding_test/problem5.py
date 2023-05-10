from sys import stdin
from collections import deque

def bfs(melon, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    for i in range(n):
        for j in range(m):
            if melon[i][j] == 1:
                q.append((i, j, 0))
    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and melon[nx][ny] == 0:
                melon[nx][ny] = 1
                q.append((nx, ny, day+1))
    for i in range(n):
        for j in range(m):
            if melon[i][j] == 0:
                return -1
    return day

k = int(input())
for i in range(k):
    m,n = map(int, stdin.readline().split())
    melon = []
    for i in range(n):
        melon.append(list(map(int, input().split())))
    print(bfs(melon, n, m))

