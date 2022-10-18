# 1949. [모의 SW 역량테스트] 등산로 조성

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# x, y: 봉우리 좌표, cur_cnt: 현재 등산로의 길이, is_built: 공사 진행 여부
def dfs(x, y, cur_cnt, is_built):
    is_done = True                                                              # 더 이상 갈 곳이 있는가??
    for d in range(4):
        move_x, move_y = x + dx[d], y + dy[d]
        if 0 <= move_x < N and 0 <= move_y < N and not visited[move_x][move_y]:  # 유효성 검사 통과 및 미방문 시
            if matrix[x][y] > matrix[move_x][move_y]:                            # 내려가는 지형일 경우
                visited[move_x][move_y] = True                                   # 방문 처리
                dfs(move_x, move_y, cur_cnt + 1, is_built)                       # 재귀 진행
                visited[move_x][move_y] = False                                  # 방문 처리 취소
                is_done = False                                                  # 아직 갈 곳이 있다!

            # 아직 공사를 진행한 적 없고 공사했을 때 내려가는 지형을 만들 수 있다면
            elif not is_built and matrix[x][y] > matrix[move_x][move_y] - K:

                temp = matrix[move_x][move_y]               # 공사 진행할 위치의 높이 저장
                matrix[move_x][move_y] = matrix[x][y] - 1   # 공사 진행(중요: K만큼 깎는 게 아니라 이전 위치 크기 - 1만큼만!)
                visited[move_x][move_y] = True              # 방문 처리
                dfs(move_x, move_y, cur_cnt + 1, True)      # 재귀 진행
                visited[move_x][move_y] = False             # 방문 처리 취소
                matrix[move_x][move_y] = temp               # 공사 진행하기 전의 높이로 되돌려놓기
                is_done = False                             # 아직 갈 곳이 있다!

    if is_done:                     # 주위를 탐색했을 때 더 이상 진행할 곳이 없다면
        global max_cnt
        if max_cnt < cur_cnt:       # 누적된 등산로의 최대 길이와 현재 길이 비교
            max_cnt = cur_cnt


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    peaks = []                                      # 봉우리 위치 리스트
    max_cnt = 0                                     # 가장 긴 등산로의 길이
    max_peak = 0                                    # 가장 높은 봉우리의 크기

    for i in range(N):                              # matrix에 지도 정보를 넣어주는 반복문
        row = list(map(int, input().split()))

        for j in range(N):
            if row[j] > max_peak:                   # 현재 저장된 봉우리 크기보다 크다면
                max_peak = row[j]                   # 봉우리 크기 갱신
                peaks = [(i, j)]                    # 봉우리 리스트 초기화

            elif row[j] == max_peak:                # 현재 저장된 봉우리 크기와 같다면
                peaks.append((i, j))                # 봉우리 리스트에 추가
        matrix.append(row)

    visited = [[False] * N for _ in range(N)]       # 방문 리스트

    for peak in peaks:                              # 각 봉우리 마다 dfs 실행
        visited[peak[0]][peak[1]] = True            # 방문 처리
        dfs(*peak, 1, False)
        visited[peak[0]][peak[1]] = False           # 방문 처리 취소

    print(f"#{tc} {max_cnt}")
