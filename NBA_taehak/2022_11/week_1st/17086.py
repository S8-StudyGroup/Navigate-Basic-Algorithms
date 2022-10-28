# 아기상어2
from collections import deque
import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

# 상어위치
sharks = []
for r in range(n):
    for c in range(m):
        if area[r][c] == 1:
            sharks.append((r, c))


dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
INF = 99999999
distance = [[INF] * m for _ in range(n)]


def bfs_dij(shark):
    queue = deque()
    queue.append(shark)
    distance[shark[0]][shark[1]] = 0
    while queue:
        r, c = queue.popleft()

        for di in range(8):
            nr = r + dr[di]
            nc = c + dc[di]

            if 0 <= nr < n and 0 <= nc < m and distance[nr][nc] > distance[r][c] + 1:
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))


for shark in sharks:
    bfs_dij(shark)


result = max(list(map(max, distance)))
print(result)