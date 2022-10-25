# [BOJ] 16236. 아기 상어

from collections import deque

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):  # 상어의 위치 찾음
    for y in range(n):
        if sea[x][y] == 9:
            sx, sy = x, y

sea[sx][sy] = 0  # 상어의 처음 위치를 찾고 난 후에는 그 자리를 0으로 표시

shark = 2  # 아기 상어 처음 크기
fish_cnt = 0  # 먹은 물고기 수
time_cnt = 0  # 아기 상어가 혼자 물고기를 잡아 먹는 시간

# 상, 좌, 하, 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

find_queue = deque()  # 이동 가능한 좌표
fish_queue = deque()  # 물고기~

visited = [[False] * n for _ in range(n)]  # 확인 여부
find_queue.append((sx, sy, 0))  # 현재 상어의 위치 추가
min_dis = -1

while find_queue:  # 이동 가능한 좌표가 있을 때,
    nx, ny, dis = find_queue.popleft()  # 하나씩 꺼내서 (우선순위 순)
    visited[sx][sy] = True  # 확인여부 체크하고

    if fish_cnt == shark:  # 상어 크기만큼 물고기를 먹었으면
        shark += 1  # 진화
        fish_cnt = 0

    if min_dis != dis:
        for d in range(4):
            if 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < n:  # 범위 내
                if not visited[nx + dx[d]][ny + dy[d]]:  # 아직 확인 안한

                    if (
                        sea[nx + dx[d]][ny + dy[d]] == 0
                        or sea[nx + dx[d]][ny + dy[d]] == shark
                    ):  # 통과 가능한 곳(경로찾기 ing)
                        find_queue.append(
                            (nx + dx[d], ny + dy[d], dis + 1)
                        )  # find_queue 에 넣어줌
                        visited[nx + dx[d]][ny + dy[d]] = True

                    elif 0 < sea[nx + dx[d]][ny + dy[d]] < shark:  # 먹을 수 있는 물고기
                        if not fish_queue:  # 첫 번째로 넣는 물고기까지의 거리를 min_dis 로 저장
                            min_dis = dis + 1
                        fish_queue.append((nx + dx[d], ny + dy[d], dis + 1))

    if (
        min_dis == dis or not find_queue
    ):  # 먹을 수 있는 물고기가 있을 때(min_dis > 0) 그 거리만큼을 다 탐색한 후
        if fish_queue:
            sx, sy, dis = fish_queue.popleft()  # 첫 번째 물고기 꺼내서
            fish_cnt += 1  # 먹은 물고기 수 + 1
            time_cnt += dis  # 이동거리(시간) 추가

            if fish_queue:  # 확인할 물고기가 더 남았다면
                for fx, fy, dis in fish_queue:  # 순서대로 꺼내서
                    if fx < sx:  # 위쪽 우선순위 따지고
                        sx = fx
                        sy = fy
                    elif fx == sx:
                        if fy < sy:  # 왼쪽 우선순위 따짐
                            sx = fx
                            sy = fy

            sea[sx][sy] = 0  # 물고기 위치는 0으로 갱신
            min_dis = -1
            # print(sx, sy, time_cnt)
            find_queue = deque()  # find_queue 초기화
            fish_queue = deque()  # fish_queue 초기화
            find_queue.append((sx, sy, 0))  # 다시 현재 상어 위치를 find_queue 에 넣어줌
            visited = [[False] * n for _ in range(n)]  # visited 초기화

print(time_cnt)
