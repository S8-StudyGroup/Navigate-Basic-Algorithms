# 1949_등산로 조성

import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# dfs 함수 ((int)행 좌표, (int)열 좌표, (Boolean)공사를 했는지 확인할 변수)
def dfs(i, j, cut):
    global road_length
    global max_road_length
    visited[i][j] = True                    # 방문표시
    road_length += 1                        # DFS 순회를 하면서 거쳐온 등산로의 길이를 저장

    if road_length > max_road_length:       # 등산로 길이의 최대값을 최신화
        max_road_length = road_length

    for direction in range(4):              # 델타 검색
        next_i = i + di[direction]          # 다음 방향의 행 좌표
        next_j = j + dj[direction]          # 다음 방향의 열 좌표

        # 다음 등산로가 범위 내에 있고, 방문하지 않은 곳이라면
        if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j]:
            # 다음 등산로가 현재 위치보다 더 낮다면 DFS 수행
            if mountains[next_i][next_j] < mountains[i][j]:
                dfs(next_i, next_j, cut)

                # 깊이 탐색이 끝나고 되돌아가는 부분
                visited[next_i][next_j] = False         # 이미 탐색한 위치는 방문표시를 제거
                road_length -= 1                        # 방문 표시를 제거하면서 길이도 원상복구 
            else:
                if mountains[next_i][next_j] - K < mountains[i][j] and not cut:     # 공사가 가능하고, 공사를 하지 않았다면
                    cut = True                                                      # 공사를 진행한다는 표시
                    cut_length = mountains[next_i][next_j] - mountains[i][j] + 1    # 현재 봉우리보다 1 낮은 높이로
                    mountains[next_i][next_j] -= cut_length                         # 봉우리 공사를 진행
                    dfs(next_i, next_j, cut)                                        # 다음 봉우리를 탐색

                    # 깊이 탐색이 끝나고 되돌아가는 부분
                    road_length -= 1                            # 길이를 원상복구
                    cut = False                                 # 공사가 가능하게 복구
                    visited[next_i][next_j] = False             # 방문표시 제거
                    mountains[next_i][next_j] += cut_length     # 봉우리 높이도 복구


for test_case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    mountains = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0

    # 모든 산을 탐색하면서 가장 높은 봉우리들을 찾음
    for i in range(N):
        for j in range(N):
            if mountains[i][j] > max_height:
                max_height = mountains[i][j]        # max_height 에 저장

    # 모든 산을 다시 탐색하면서 가장 높은 봉우리를 만났을 때 DFS 수행
    max_road_length = 0
    for i in range(N):
        for j in range(N):
            if mountains[i][j] == max_height:
                start_i = i
                start_j = j
                road_length = 0
                visited = [[False] * N for _ in range(N)]
                dfs(start_i, start_j, False)
    
    # 출력
    print(f'#{test_case} {max_road_length}')
