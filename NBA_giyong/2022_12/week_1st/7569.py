# [BOJ] 7569. 토마토(3차원)
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        a, b, c = q.popleft()
        visited[c][a][b] = 1
        for w in range(6):
            x = a + dx[w]
            y = b + dy[w]
            z = c + dz[w]
            if 0 <= x < n and 0 <= y < m and 0 <= z < h and tomato[z][x][y] == 0 and visited[z][x][y] == 0:
                q.append([x, y, z])
                tomato[z][x][y] = tomato[c][a][b] + 1       # 날짜를 세기 위해서
                visited[z][x][y] = 1


m, n, h = map(int, input().split())
tomato = [[] for _ in range(h)]                                             # 토마토를 담을 빈 리스트 생성
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]     # 방문했는지 확인
q = deque([])
result = 0

for i in range(h):
    for j in range(n):
        tomato[i].append(list(map(int, input().split())))   # 문제에 주어진 토마토를 가져오고

for d in range(h):
    for f in range(n):
        for e in range(m):
            if tomato[d][f][e] == 1:    # 익은 토마토의 위치를 나타낸다
                q.append([f, e, d])     # 시작할 토마토 위치를 넣어준다

# print(tomato)

bfs()

# print(tomato)

day = 0                                 # 토마토가 다 익을 수 있는 최대값
for d in range(h):
    for f in range(n):
        for e in range(m):
            if tomato[d][f][e] == 0:        # 안익은 토마토가 있으면
                result = -1
            day = max(day, tomato[d][f][e])

if result == 0:
    print(day - 1)
else:
    print(result)
