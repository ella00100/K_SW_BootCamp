from collections import deque
import sys

def bfs(col, row, map_data, n_room):
    start_col = col
    start_row = row
    queue = deque()

    queue.append((col, row, []))

    while queue:
        col, row, visit = queue.popleft()

        if len(visit) == n_room and start_col == col and start_row == row:
            return True

        for d_col, d_row in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_col = col + d_col
            next_row = row + d_row

            if 0 <= next_col < m and 0 <= next_row < n and map_data[next_col][next_row] == 0:
                if ((col, row), (next_col, next_row)) not in visit and (next_col, next_row) not in visit:
                    queue.append((next_col, next_row, visit + [((col, row), (next_col, next_row))]))

    return False


T = int(sys.stdin.readline())

for _ in range(T):
    n_room = 0
    n, m = map(int, sys.stdin.readline().split())

    map_data = []
    for _ in range(m):
        row = list(map(int, sys.stdin.readline().split()))
        map_data.append(row)

        for cell in row:
            if cell == 0:
                n_room += 1

    is_escape = False
    for col in range(m):
        for row in range(n):
            if map_data[col][row] == 0:
                if bfs(col, row, map_data, n_room):
                    is_escape = True
                    break
        if is_escape:
            break

    if is_escape:
        print(1)
    else:
        print(0)