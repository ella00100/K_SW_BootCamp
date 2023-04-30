import sys

w, h = map(int, input().split())
array = []

for _ in range(h):
    array.append(list(map(int, input().split())))

def DFS(i, j, w, h, array, visited):
    if visited[i][j]:
        return 0
    if array[i][j] == 1:
        return 0

    visited[i][j] = True
    for dx, dy in [[-1,-1], [-1,0], [-1,1],
                   [0,-1], [0,1],
                   [1,-1], [1,0], [1,1]]:
        nx = i + dx
        ny = j + dy

        if 0<= nx < h and 0 <= ny < w:
            if array[nx][ny] == 1:
                DFS(nx, ny, w, h, array, visited)

    return 1



