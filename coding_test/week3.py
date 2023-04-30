#섬의 개수
import sys
sys.setrecursionlimit(10000)

def DFS(i, j, w, h, array, visited):
    if visited[i][j]:
        return 0
    if array[i][j]:
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

def solution(w, h, array):
    answer = 0
    visited =[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                answer = answer + DFS(i, j, w, h, array, visited)

    return answer

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    array = []
    for _ in range(h):
        array.append(list(map(int, input().split())))

    answer = solution(w, h, array)
    print(answer)