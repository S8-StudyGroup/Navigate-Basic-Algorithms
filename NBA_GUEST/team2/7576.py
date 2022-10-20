# [BOJ] 7576. 토마토
# Guest - 김경아

from collections import deque


# 인접한 토마토 찾기
def search(x, y, tomato):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1          # 인접한 토마토 익히기 (하루 미리 익힘 표시)
            tomato.append((nx, ny))  # 다음 날 익을 토마토의 좌표를 튜플로 리스트에 담기


# 상, 하, 좌, 우 (익힐 수 있는 토마토 범위)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# input 값 받기
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
day = -1          # 첫 날 익은 토마토(1)의 위치를 넣고 시작할 것이기 때문에 첫 날 count는 무효화
tomato = deque()  # 다음날 익을 토마토를 담을 리스트


# 익은 토마토 위치 담기
for x, list_box in enumerate(box):
    for y in range(m):
        if list_box[y] == 1:
            tomato.append((x, y))     # tomato = [(4, 5)]


while tomato:                         # 리스트가 빌 때까지 반복
    cnt = len(tomato)                 # (같은 날 익은 토마토를 체크하기 위함) cnt = 1
    for _ in range(cnt):              # 같은 날 익은 토마토 개수만큼 반복
        result = tomato.popleft()     # deque의 맨 왼쪽에 있는 값 꺼내기 # result = (4, 5)
        x, y = result[0], result[-1]  # x = 4, y = 5
        search(x, y, tomato)
    day += 1                          # 다 담으면 다음날이 됨


for check in box:                     # 박스들 다 돌았는데 안 익은 토마토가 있다면 -1을 출력
    if 0 in check:
        day = -1
        break

print(day)
