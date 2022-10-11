# [BOJ] 7576. 토마토

from collections import deque   # deque을 이용하기 위한 import문

dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 델타이동
dy = [1, 0, -1, 0]


def bfs():
    global queue

    max_cnt = 0             # 최소 일수
    queue = deque(queue)    # 큐에는 익은 토마토 위치를 모두 저장해놔있음

    while queue:
        px, py = queue.popleft()    # 큐에서 하나씩 뽑아서

        for k in range(4):
            nx = px + dx[k]         # 해당 자리의 상하좌우의 위치를 알아보고
            ny = py + dy[k]

            # 범위 안이고, 아직 방문하지 않은 것들 중 0(덜 익은 토마토)인 경우
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))                  # 다음으로 익을 토마토로 지정하여 큐에 저장
                visited[nx][ny] = visited[px][py] + 1   # 익는데 걸린 시간은 인접해 있던 익은 토마토가 걸린 시간 + 1

                if visited[nx][ny] > max_cnt:           # visited에 숫자를 넣을 때마다 max 일수로서 업데이트
                    max_cnt = visited[nx][ny]

    return max_cnt - 1


m, n = map(int, input().split())        # 보관함 가로 길이 m, 세로 길이 n
zero_cnt = 0                            # 0의 개수 : 안 익은 토마토 개수
arr = []                                # 토마토 보관함 이차원리스트
queue = []                              # BFS에서 사용할 큐
visited = [[0] * m for _ in range(n)]   # 방문 리스트

for r in range(n):
    row = list(map(int, input().split()))   # 행 한 줄마다 받고
    for c in range(m):
        if row[c] == 1:                     # 행의 열마다 돌면서 1(익은 토마토) 자리를 큐에 저장
            queue.append((r, c))
            visited[r][c] = 1               # 방문 리스트의 해당 자리에 1 저장
        if row[c] == 0:                     # 만약 해당 자리가 0이면
            zero_cnt += 1                   # 0의 개수 +1
    arr.append(row)                         # 작업을 마친 행마다 arr에 저장

if zero_cnt == 0:   # 만약 덜 익은 토마토가 없으면
    answer = 0      # 결과는 0으로 출력
else:               # 덜 익은 토마토가 하나라도 있으면
    answer = bfs()  # bfs 함수 실행

breaker = False     # 중간에 멈추게 해 줄 breaker 선언

for i in range(n):
    if breaker == False:
        for j in range(m):
            if arr[i][j] == 0 and visited[i][j] == 0:   # 방문리스트, 이차원리스트가 동시에 0이면
                answer = -1                             # 결과를 -1으로 해주고 중단
                breaker = True
                break

print(answer)
