# [BOJ] 7576. 토마토
# Guest - 박윤지

from collections import deque

# 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
# 열 , 행
m, n = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]

ripe_tomato = deque()  # 익은 토마토 저장할 큐, 리스트로 pop(0) 하니까 시간초과남
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:  # 익은 토마토
            ripe_tomato.append((i, j))

# 익은 토마토들을 시작으로 bfs 진행
while ripe_tomato:  # 값이 있는 동안
    x, y = ripe_tomato.popleft()  # 현재 토마토 지점
    for direction in range(4):  # 델타 검색으로 이동
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 박스 범위 안이고 안익은 토마토를 발견한다면
        if 0 <= nx < n and 0 <= ny < m and boxes[nx][ny] == 0:
            boxes[nx][ny] = boxes[x][y] + 1  # 토마토 자리에 익은 날짜 적어주기
            ripe_tomato.append((nx, ny))  # 익은 토마토 저장

max_day = 0
for i in range(n):
    for j in range(m):
        # 안익은 토마토가 있으면 다 닿지 못한 것
        if boxes[i][j] != 0:
            if max_day < boxes[i][j]:  # 제일 큰 날짜 구해주기
                max_day = boxes[i][j]
        else:  # -1 출력후 종료
            print(-1)
            exit(0)
        # exit(0) means a clean exit without any errors / problems
        # exit(1) means there was some issue / error / problem and that is why the program is exiting.

print(max_day - 1)  # 1일차부터 시작했기 때문에 하루 빼주기

# 처음엔 모두 이미 익어있는 토마토인 경우(0 출력)를 따로 예외처리하려고 했는데
# max_day = 1 이고 1-1 = 0 이 나오므로 따로 구하지 않아도 된다
