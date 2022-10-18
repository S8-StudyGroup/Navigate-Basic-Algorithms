# [BOJ] 7576. 토마토

import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr):                                                       # arr: 익은 토마토 리스트
    visited = [[-1] * M for _ in range(N)]                          # 방문 리스트(-1로 초기화) == 보관 후 지난 날짜
    cnt = 0                                                         # 익은 토마토 개수
    for x, y in arr:                                                # 익은 토마토들에 대하여
        visited[x][y] = 0                                           # 해당 위치를 방문 처리하고
        cnt += 1                                                    # 익은 토마토 개수 + 1해주기!
    queue = deque(arr)                                              # 익은 토마토 리스트를 덱에 넣고 bfs 돌리기!

    while queue:
        if cnt == total_cnt:                                        # 현재까지의 익은 토마토 개수가 총 토마토 개수와 같다면
            max_day = 0
            for i in range(N):
                for j in range(M):
                    if max_day < visited[i][j]:                     # 방문 리스트에서 가장 큰 숫자를 찾아서
                        max_day = visited[i][j]
            return max_day                                          # 반환(토마토가 다 익는 최소 일수)

        x, y = queue.popleft()                                      # 덱에서 익은 토마토 꺼냄!
        for d in range(4):                                          # 델타탐색
            move_x, move_y = x + dx[d], y + dy[d]
            if (
                0 <= move_x < N
                and 0 <= move_y < M                                 # 유효성 검사를 통과하고
                and storage[move_x][move_y] == 0                    # 익지 않은 토마토이며
                and visited[move_x][move_y] == -1                   # 방문하지 않았다면
            ):
                visited[move_x][move_y] = visited[x][y] + 1         # 익은 시점의 날짜로 방문 처리
                cnt += 1                                            # 익은 토마토 개수 + 1
                queue.append((move_x, move_y))                      # 덱에 삽입

    return -1


M, N = map(int, input().split())
storage = []
ripe_tomatoes = []                          # 익은 토마토 리스트
total_cnt = M * N                           # 총 토마토 개수(가로 * 세로)

for i in range(N):                          # storage에 토마토들 넣어주는 작업
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:                     # 익은 토마토라면
            ripe_tomatoes.append((i, j))    # 익은 토마토 리스트에 추가
        elif row[j] == -1:                  # 해당 칸이 비어있다면
            total_cnt -= 1                  # 총 토마토 개수 - 1
    storage.append(row)

print(bfs(ripe_tomatoes))
