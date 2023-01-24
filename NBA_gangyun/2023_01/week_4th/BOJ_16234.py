# BOJ_16234. 인구 이동
from collections import deque
from copy import deepcopy
import sys


def bfs(i, j):
    visited[i][j] = True

    queue = deque()
    queue.append((i, j))
    open_boundary = []
    sum_population = 0

    while queue:
        i, j = queue.popleft()
        sum_population += ground[i][j]
        compare = ground[i][j]
        open_boundary.append((i, j))
        for direction in range(4):
            check_i = i + di[direction]
            check_j = j + dj[direction]
            if (
                0 <= check_i < N and 0 <= check_j < N and
                L <= abs(compare - ground[check_i][check_j]) <= R
                and not visited[check_i][check_j]
            ):
                visited[check_i][check_j] = True
                queue.append((check_i, check_j))

    countries = len(open_boundary)
    for point in open_boundary:
        ground[point[0]][point[1]] = sum_population // countries


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

input = sys.stdin.readline
N, L, R = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
count = 0

while True:
    old_ground = deepcopy(ground)
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    if old_ground == ground:
        break
    count += 1

print(count)
