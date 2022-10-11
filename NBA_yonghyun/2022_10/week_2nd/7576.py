# [BOJ] 7576. 토마토

# 리스트를 사용하는 것 보다는 deque를 사용하면 훨씬 더 빠르다!!!

from collections import deque

import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, day):
    queue = deque()
    tomato = 0      # 익은 토마토의 수 + 빈 칸의 수

    # 초기 익은 토마토 전부 queue 에 저장
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                queue.append((i, j, 0))
                tomato += 1
            elif box[i][j] == -1:
                tomato += 1

    # 보관 시에 이미 모두 익어있으면,
    if len(queue) == m * n:
        return 0

    # 모든 큐에 있는 토마토를 확인할 때까지
    while queue:
        x, y, day = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < m and 0 <= ny < n:             # 상자의 범위 내에 있고
                if box[nx][ny] == 0:                    # 익지 않은 토마토면서
                    queue.append((nx, ny, day + 1))     # 새로 익은 토마토 queue 에 저장
                    box[nx][ny] = 1                     # 토마토 익음 표시
                    tomato += 1

    if tomato != m * n:         # 익지 않은 토마토가 남아 있을 때
        return -1
    else:                       # 전부 익었을 때
        return day


n, m = map(int, input().split())        # 세로, 가로
box = [list(map(int, input().split())) for _ in range(m)]
print(bfs(0, 0, 0))
