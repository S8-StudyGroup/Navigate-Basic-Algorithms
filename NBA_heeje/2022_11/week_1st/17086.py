# [BOJ] 17086. 아기 상어 2

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def bfs(queue):
    safe_zone = N * M - len(queue)
    queue = deque(queue)
    while queue:
        x, y = queue.popleft()

        for d in range(8):
            move_x, move_y = x + dx[d], y + dy[d]

            if 0 <= move_x < N and 0 <= move_y < M and matrix[move_x][move_y] == 0:
                matrix[move_x][move_y] = matrix[x][y] + 1
                safe_zone -= 1

                if safe_zone == 0:
                    return matrix[move_x][move_y] - 1

                queue.append((move_x, move_y))


N, M = map(int, input().split())
matrix = []
baby_shark_list = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            baby_shark_list.append((i, j))
    matrix.append(row)

print(bfs(baby_shark_list))
