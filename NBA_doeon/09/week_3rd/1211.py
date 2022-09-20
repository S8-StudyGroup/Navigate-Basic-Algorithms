# [SWEA] 1211. Ladder2

import copy


def dfs(x, y):
    global cnt
    global min_cnt
    global min_pos

    if cnt > min_cnt:           # 가지치기 (벌써 현재 min_cnt를 넘은 경로의 경우, cnt 세기 중단)
        return

    new_visited[x][y] = True    # 여기로 들어왔다는 방문 처리 해주고
    cnt += 1                    # 한 칸 왔으니까 cnt + 1 처리

    # 좌,우,하 순서로 그 칸에 접근할 수 있는지 for문으로 확인하고 접근
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1 and not new_visited[nx][ny]:
            # 1) 만약 다음으로 갈 칸이 마지막 행이면
            if nx == 99:    # 99행이면 도착했단 거니까
                if cnt < min_cnt:   # 이 출발점의 cnt가 min_cnt보다 작다면
                    min_cnt = cnt   # min_cnt 갱신
                    min_pos = s     # 최소 경로 출발점 갱신
                return              # 모든 갱신 후 함수 종료

            # 2) 아직 안 끝났으면 해당 새로운 칸에서 쭉 가게 함
            dfs(nx, ny)


dx = [0, 0, 1]  # 좌, 우, 하 델타값 (순서 중요! 좌우를 우선적으로 가고 아래로 가기 때문)
dy = [-1, 1, 0] # 좌, 우, 하

for _ in range(1, 11):
    tc = int(input())
    min_cnt = 10000 # 초기 최소값
    min_pos = 99    # 초기 최소값 출발점

    ladder = [list(map(int, input().split())) for _ in range(100)]  # 사다리 정보
    visited = [[False] * 100 for _ in range(100)]   # 방문리스트

    for s in range(99, -1, -1): # 출발점 99 인덱스에서부터 for문으로 경로 탐색
        new_visited = copy.deepcopy(visited)    # 각 출발점마다 방문리스트 초기화(해주지 않으면 다음 출발점의 경로 때, 문제 발생)
        if ladder[0][s] == 1:   # 0행에서 s번째 열의 칸 값이 1이면 거기서 출발 가능!
            cnt = 0     # 각 출발점마다의 초기 cnt
            dfs(0, s)   # s에서 출발하는 함수 실행

    print(f'#{tc} {min_pos}')
