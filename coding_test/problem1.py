from sys import stdin

def dfs(x, y, visited):
    visited[x][y] = True
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and cube[nx][ny] != 1:
            dfs(nx, ny, visited)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cube = [list(map(int, stdin.readline().split())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    dfs(0, 0, visited)

    if visited[0][0] and visited[n-1][m-1]:
        print()
        print(1)
    else:
        print()
        print(0)