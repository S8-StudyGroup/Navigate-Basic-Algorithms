# [BOJ] 7576. 토마토
from collections import deque

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def is_tomato_cooked(house):
    for i in range(row):
        for j in range(col):
            if house[i][j] == 0:
                return False
    return True


def bfs(tomatoes):
    global depth
    queue = deque()
    for i, j in tomatoes:
        queue.append((i, j, depth))

    while queue:
        temp_i, temp_j, depth = queue.popleft()

        for direction in range(4):
            ni = temp_i + di[direction]
            nj = temp_j + dj[direction]

            if 0 <= ni < row and 0 <= nj < col and house[ni][nj] == 0:
                house[ni][nj] = 1
                queue.append((ni, nj, depth + 1))


col, row = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(row)]

depth = 0
cooked = []

for i in range(row):
    for j in range(col):
        if house[i][j] == 1:
            cooked.append((i, j))

bfs(cooked)

if is_tomato_cooked(house):
    print(depth)
else:
    print(-1)
