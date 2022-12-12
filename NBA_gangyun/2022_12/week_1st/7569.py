# [BOJ] 7569. 토마토(3차원)

from collections import deque

di = [0, 0, -1, 0, 1, 0]
dj = [0, 0, 0, 1, 0, -1]
dk = [-1, 1, 0, 0, 0, 0]


def bfs(tomatoes):
    global depth
    queue = deque()
    for (k, i, j) in tomatoes:
        visited[k][i][j] = True
        queue.append((k, i, j, depth))

    while queue:
        temp_k, temp_i, temp_j, depth = queue.popleft()

        for direction in range(6):
            next_k = temp_k + dk[direction]
            next_i = temp_i + di[direction]
            next_j = temp_j + dj[direction]
            if 0 <= next_k < height and 0 <= next_i < row and 0 <= next_j < col and not visited[next_k][next_i][next_j] and box[next_k][next_i][next_j] != -1:
                visited[next_k][next_i][next_j] = True
                box[next_k][next_i][next_j] = 1
                queue.append((next_k, next_i, next_j, depth + 1))

    return depth


col, row, height = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(row)] for _2 in range(height)]

visited = [[[False] * col for _ in range(row)] for _2 in range(height)]
tomatoes = []
not_cooked_count = 0

for k in range(height):
    for i in range(row):
        for j in range(col):
            if box[k][i][j] == 1:
                tomatoes.append((k, i, j))
            if box[k][i][j] == 0:
                not_cooked_count += 1

if not_cooked_count == 0:
    print(0)
else:
    depth = 0
    bfs(tomatoes)
    for k in range(height):
        for i in range(row):
            for j in range(col):
                if box[k][i][j] == 0:
                    print(-1)
                    exit()
    print(depth)