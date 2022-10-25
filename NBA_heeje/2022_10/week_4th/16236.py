# [BOJ] 16236. 아기 상어

import sys
input = sys.stdin.readline


def bfs(s):
    queue = [s]
    distance = [[0] * N for _ in range(N)]              # 거리에 대한 이차원 리스트
    distance[s[0]][s[1]] = 1                            # 현재 위치의 거리를 1로 지정
    min_dis = 400                                       # 먹을 수 있는 물고기까지의 최소 거리
    min_dis_x, min_dis_y = N, N                         # 그 물고기의 좌표

    while queue:
        x, y = queue.pop(0)

        if distance[x][y] - 1 < min_dis:                        # 최소 거리보다 작을 때만 진행
            for d in range(4):                                  # 델타탐색
                move_x, move_y = x + dx[d], y + dy[d]
                if (
                    0 <= move_x < N                              # 유효성 검사를 통과하고
                    and 0 <= move_y < N
                    and distance[move_x][move_y] == 0            # 가지 않은 곳이면서
                    and matrix[move_x][move_y] <= baby_shark     # 상어의 크기보다 작거나 같은 곳일 때
                ):
                    if 0 < matrix[move_x][move_y] < baby_shark:  # 해당 위치에 먹을 수 있는 물고기가 있다면
                        min_dis = distance[x][y]                 # 최소 거리 설정
                        
                        if move_x < min_dis_x:                              # 물고기의 좌표 비교
                            min_dis_x, min_dis_y = move_x, move_y
                        elif move_x == min_dis_x and move_y < min_dis_y:
                            min_dis_y = move_y

                    distance[move_x][move_y] = distance[x][y] + 1   # 거리 증가
                    queue.append((move_x, move_y))                  # 큐에 삽입

    if min_dis_x < N:                           # 큐를 다 돌았을 때 먹을 수 있는 물고기가 있다면
        return min_dis_x, min_dis_y, min_dis    # 해당 물고기의 좌표와 이동 거리를 반환


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())

matrix = []                                     # 이차원 리스트
baby_shark = 2                                  # 상어의 초기 크기
cnt_eaten_fish = 0                              # 먹은 물고기의 개수
time = 0                                        # 답

# 이차원 리스트에 공간의 상태를 저장하면서 상어의 위치까지 저장
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            start = (i, j)
    matrix.append(row)

while True:
    # 먹을 수 있는 물고기가 있다면 해당 위치와 걸린 시간을 play에 저장하고, 없다면 None이 play에 저장됨
    play = bfs(start)
    if play:                                # play가 None이 아니라면
        shark_x, shark_y, dt = play         # 상어의 좌표와 걸린 시간을 받아온 뒤
        matrix[start[0]][start[1]] = 0      # 상어의 원래 위치를 0으로 바꿔준 후
        start = shark_x, shark_y            # bfs 시작 위치를 새로운 상어의 좌표로 정해준다!
        time += dt                          # 걸린 시간을 최종 시간에 더해주고
        cnt_eaten_fish += 1                 # 먹은 물고기 수 + 1
        matrix[shark_x][shark_y] = 9        # 새로운 상어 위치 지정

        if baby_shark == cnt_eaten_fish:    # 만약 아기 상어의 크기와 먹은 물고기 수가 같다면
            baby_shark += 1                 # 아기 상어의 크기 + 1
            cnt_eaten_fish = 0              # 먹은 물고기 수 초기화

    else:                                   # play가 None이라면 먹을 수 있는 물고기가 없다는 것이므로
        break                               # 반복문 탈출

print(time)
