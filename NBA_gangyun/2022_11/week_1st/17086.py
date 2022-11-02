# BOJ_17086. 아기상어2

from collections import deque

# 상 우상 우 우하 하 좌하 좌 좌상
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(i, j):

    global depth
    depth -= 1
    queue = deque()
    queue.append((i, j, depth))
    visited[i][j] = True

    while queue:
        temp_i, temp_j, depth = queue.popleft()

        for direction in range(8):
            next_i = temp_i + di[direction]
            next_j = temp_j + dj[direction]
            if 0 <= next_i < row and 0 <= next_j < col and not visited[next_i][next_j]:
                if space[next_i][next_j] != 1:
                    visited[next_i][next_j] = True
                    if space[next_i][next_j] == 0:
                        space[next_i][next_j] = depth
                    else:
                        if depth > space[next_i][next_j]:
                            space[next_i][next_j] = depth
                    queue.append((next_i, next_j, depth - 1))


row, col = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(row)]
max_distance = 0
visited = [[False] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        if space[i][j] == 1 and not visited[i][j]:
            depth = 0
            visited = [[False] * col for _ in range(row)]
            bfs(i, j)


for i in range(row):
    for j in range(col):
        if space[i][j] < max_distance:
            max_distance = space[i][j]

print(-max_distance)