# [BOJ] 16236. 아기 상어

dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]  # 우하좌상


def bfs(x, y):
    global size, time, cnt_fish             # bfs 돌 때마다 바뀌어질 값 -> global 변수로 선언

    visited = [[0] * n for _ in range(n)]   # 상어 위치 초기화될 때마다 visited 리스트도 초기화
    visited[x][y] = 1                       # x, y로 들어온 상어 위치를 1로 표시 (추후에 -1 처리)
    queue = []                              # 빈 큐를 만들어
    can_eat = []                            # 레이더망에 걸리는 물고기 위치들 다 저장해놓을 곳
    
    queue.append((x, y))
    is_fish = False
    first_done = False

    # 1. 물고기 후보지 저장
    while queue:

        px, py = queue.pop(0)

        # 1) 먹을 수 있는 물고기가 있고, 아직 첫 물고기 못 찾은 상태인 경우
        if 0 < sea[px][py] < size and first_done == False:  
            is_fish = True                      # 물고기 있는 곳 찾았어! 말해주고
            cur_dist = visited[px][py]          # 물고기 발견 위치의 거리 저장(이 거리의 물고기 이외엔 보지 않으므로)
            first_done = True
            can_eat.append((px, py))            # 물고기 후보지에 저장


        # 2) 먹을 수 있는 물고기가 있고, 첫 물고기와 같은 거리의 있는 애들인 경우에 한해
        elif 0 < sea[px][py] < size and visited[px][py] == cur_dist:
            can_eat.append((px, py))            # 물고기 후보지에 저장


        # 3) 아직 첫 물고기 못 찾았을 동안 계속 그 인접칸 큐에 넣기
        elif is_fish == False:
            for k in range(4):      # 우하좌상 모든 방향에 대해서
                nx = px + dx[k]
                ny = py + dy[k]

                if 0 <= nx < n and 0 <= ny < n and sea[nx][ny] <= size and visited[nx][ny] == 0: # 그 다음칸이 이동 가능하면
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[px][py] + 1       # 거리 표현을 위해 그 부모 위치보다 +1로 visited 표시

    # while문 끝나면
    # can_eat에 같은 거리의 물고기 후보지 저장돼있을 것

    # 2. 후보지 중 어디로 갈지 정하기
    if can_eat:
        go_i, go_j = n - 1, n - 1
        for idx, _ in enumerate(can_eat):   # 후보지 돌면서
            if can_eat[idx][0] < go_i:      # 후보지 i인덱스가 현재보다 작으면
                go_i = can_eat[idx][0] 
                go_j = can_eat[idx][1]      # 그 후보지를 갈 곳으로 한다

            if can_eat[idx][0] == go_i:     # 근데 후보지 i인덱스가 현재 갈 곳이랑 똑같으면
                if can_eat[idx][1] < go_j:  # 현재 갈 j 인덱스보다 작은 경우에만
                    go_i = can_eat[idx][0]  # 그 후보지로 바꿔줌
                    go_j = can_eat[idx][1]

        # 그럼 이제 어디로 갈지 확정됨!
        # 3. 후보지 확정에 따른 변경 사항 반영해주기

        sea[go_i][go_j] = 0                 # 해당 위치 물고기 먹혔으니까 0
        cnt_fish += 1                       # 먹은 물고기 수 + 1

        if cnt_fish == size:                # 몸 크기만큼 먹었다면
            size += 1                       # 크기 업
            cnt_fish = 0                    # 먹은 물고기 수 초기화

        time += visited[go_i][go_j] - 1     # 거기까지 가는데 걸리는 시간 더해주고
        sea[x][y] = 0                       # 원래 상어 있던 곳을 0으로

        return (go_i, go_j)                 # 다음 bfs를 위해 갈 곳을 return

    else:   # can_eat이 빈 리스트면 먹을 물고기 없으므로 중단
        return


n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]

# 매번 레이더 켤 때마다 초기화 되면 안되는 변수
size = 2                    # 상어 초기 크기
time = 0                    # 총 걸린 시간
cnt_fish = 0                # 먹은 물고기 개수

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:  # 상어 위치를 si, sj에 저장
            si, sj = i, j

while True:
     shark = bfs(si, sj)

     if shark:              # 반환 값(더 갈 곳이 있다면)이 있으면 반복
         si, sj = shark
     else:                  # 없으면 중단
         break

print(time)