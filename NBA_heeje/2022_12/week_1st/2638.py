# [BOJ] 2638. 치즈

import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 치즈 외부 공기들의 값을 2로 바꿔주는 함수
def outside_bfs(start):                                 # start : bfs를 실행할 첫 좌표 - (0, 0)로 고정
    copy_matrix[start[0]][start[1]] = 2                 # 초기 설정(첫 좌표의 값 2로 바꿔주기)
    queue = [start]                                     # queue에 첫 좌표 넣어줌
    while queue:                                        # queue가 빌 때까지 진행
        x, y = queue.pop(0)                             # queue에서 좌표를 꺼낸 뒤
        for d in range(4):                              # 델타 탐색
            move_x, move_y = x + dx[d], y + dy[d]       # 탐색 좌표 지정

            # 탐색 좌표가 유효성 검사를 통과하고, 비어있는 칸이면
            if 0 <= move_x < N and 0 <= move_y < M and copy_matrix[move_x][move_y] == 0:
                copy_matrix[move_x][move_y] = 2         # 해당 위치 값 2로 바꿔줌!
                queue.append((move_x, move_y))          # 큐에 탐색 좌표 삽입


N, M = map(int, input().split())
matrix = []                                     # 모눈종이
cnt_cheese = 0                                  # 치즈의 개수
for i in range(N):
    row = list(map(int, input().split()))       # 한 행
    for j in range(M):                          # 행 탐색
        if row[j] == 1:                         # 해당 위치에 치즈가 있다면
            cnt_cheese += 1                     # 치즈 개수 + 1
    matrix.append(row)                          # 모눈종이에 입력행 추가
time = 0                                        # 주어진 치즈가 모두 녹아 없어지는데 걸리는 시간

while cnt_cheese > 0:                           # 치즈의 개수가 모두 없어질 때까지 반복
    time += 1                                   # 시간 + 1
    copy_matrix = []                            # 모눈종이를 복사할 새 배열 생성
    for i in range(N):                          # 모든 행에 대하여
        copy_matrix.append(matrix[i][:])        # 복사한 리스트를 copy_matrix에 삽입(deepcopy와 동일)
    outside_bfs((0, 0))                         # 가장자리 칸에 대한 bfs 실행

    for i in range(N):                          # 모눈종이 완전탐색
        for j in range(M):
            if copy_matrix[i][j] == 1:          # 치즈를 찾으면 녹아 없어지는 치즈인지 확인
                cnt = 0                         # 외부 공기와 접촉해있는 방향 수
                for d in range(4):              # 델타 탐색
                    move_i, move_j = i + dx[d], j + dy[d]   # 탐색 좌표 지정

                    # 탐색 좌표가 유효성 검사를 통과하면서 외부 공기(2)이면
                    if 0 <= move_i < N and 0 <= move_j < M and copy_matrix[move_i][move_j] == 2:
                        cnt += 1                # 접촉 방향 수 + 1

                # 델타 탐색 이후
                if cnt >= 2:                    # 4변 중에 적어도 2변 이상이 외부 공기와 접촉해있다면
                    matrix[i][j] = 0            # 치즈가 녹아 없어짐
                    cnt_cheese -= 1             # 치즈의 개수 - 1

print(time)
