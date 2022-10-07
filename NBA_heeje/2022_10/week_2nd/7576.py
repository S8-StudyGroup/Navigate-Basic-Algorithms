# [BOJ] 7576. 토마토

import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr):
    visited = [[-1] * M for _ in range(N)]
    cnt = 0
    for x, y in arr:
        visited[x][y] = 0
        cnt += 1
    queue = deque(arr)

    while queue:
        if cnt == total_cnt:
            max_day = 0
            for i in range(N):
                for j in range(M):
                    if max_day < visited[i][j]:
                        max_day = visited[i][j]
            return max_day
        x, y = queue.popleft()
        for d in range(4):
            move_x, move_y = x + dx[d], y + dy[d]
            if (
                0 <= move_x < N
                and 0 <= move_y < M
                and storage[move_x][move_y] == 0
                and visited[move_x][move_y] == -1
            ):
                visited[move_x][move_y] = visited[x][y] + 1
                cnt += 1
                queue.append((move_x, move_y))

    return -1


M, N = map(int, input().split())
storage = []
ripe_tomatoes = []
total_cnt = M * N
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            ripe_tomatoes.append((i, j))
        elif row[j] == -1:
            total_cnt -= 1
    storage.append(row)

print(bfs(ripe_tomatoes))
