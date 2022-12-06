# [BOJ] 7569. 토마토(3차원)

import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

farm = []   # (층, 행, 열)
for height in range(H):
    farm.append([list(map(int, input().split())) for _ in range(N)])

# 토마토 위치
tomatos = []
target_cnt = 0
for r in range(N):
    for c in range(M):
        for h in range(H):
            if farm[h][r][c] == 1:
                tomatos.append((h, r, c))
            elif farm[h][r][c] == 0:
                target_cnt += 1


dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]
dh = [-1, 1, 0, 0, 0, 0]

# BFS
day = 0
tmt_cnt = 0
while tomatos:
    day += 1
    memo = []
    while tomatos:
        h, r, c = tomatos.pop()
        for di in range(6):
            nh = h + dh[di]
            nc = c + dc[di]
            nr = r + dr[di]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and farm[nh][nr][nc] == 0:
                memo.append((nh, nr, nc))
                farm[nh][nr][nc] = 1
                tmt_cnt += 1
    tomatos = memo

if tmt_cnt == target_cnt:
    print(day - 1)
else:
    print(-1)