import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
sys.setrecursionlimit(10000)

w, h = map(int, input().split())
array = []

for _ in range(w):
    array.append(list(map(int, input().split())))

def build_wall(count):
    global ans

    if count == 3:
        bfs(deepcopy(array))
        return

    for i in range(w):
        for j in range(h):
            if array[i][j] == 0:
                array[i][j] = 1
                build_wall(count + 1)
                array[i][j] = 0

def bfs(array):
    global ans

    virus = deepcopy(array)

    queue = deque()

    for i in range(w):
        for j in range(h):
            if virus[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if virus[nx][ny] == 0:
                    virus[nx][ny] = 2
                    queue.append((nx, ny))

    count = 0
    for i in range(w):
        for j in range(h):
            if virus[i][j] == 0:
                count += 1

    ans = max(ans, count)

ans = 0
build_wall(0)
print(ans)