# [BOJ] 16236. 아기 상어

import sys

input = sys.stdin.readline


def bfs(s):
    queue = [s]
    distance = [[0] * N for _ in range(N)]
    distance[s[0]][s[1]] = 1
    min_dis = 400
    min_dis_x, min_dis_y = N, N
    while queue:
        x, y = queue.pop(0)
        if distance[x][y] <= min_dis:
            for d in range(4):
                move_x, move_y = x + dx[d], y + dy[d]
                if (
                    0 <= move_x < N
                    and 0 <= move_y < N
                    and distance[move_x][move_y] == 0
                    and matrix[move_x][move_y] <= baby_shark
                ):
                    if 0 < matrix[move_x][move_y] < baby_shark:
                        min_dis = distance[x][y]
                        if move_x < min_dis_x:
                            min_dis_x, min_dis_y = move_x, move_y
                        elif move_x == min_dis_x and move_y < min_dis_y:
                            min_dis_y = move_y

                    distance[move_x][move_y] = distance[x][y] + 1
                    queue.append((move_x, move_y))

    if min_dis_x < N:
        return (min_dis_x, min_dis_y, min_dis)


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())

matrix = []
baby_shark = 2
cnt_eaten_fish = 0
time = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            start = (i, j)
    matrix.append(row)

while True:
    play = bfs(start)
    if play:
        shark_x, shark_y, dt = play
        matrix[start[0]][start[1]] = 0
        start = shark_x, shark_y
        time += dt
        cnt_eaten_fish += 1
        matrix[shark_x][shark_y] = 9

        if baby_shark == cnt_eaten_fish:
            baby_shark += 1
            cnt_eaten_fish = 0
    else:
        break

print(time)
