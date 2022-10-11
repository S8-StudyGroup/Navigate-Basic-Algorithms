# [SWEA] 1949. 등산로 조성

'''
[ 아이디어 ]

DFS + 델타이동

k만큼 깎는 것을 어떻게 사용할까?

'''


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def trail(x, y, h, c):
    global max_length
    global cut

    if c > max_length:        # 최대 등산로 길이 갱신
        max_length = c

    for d in range(4):        # 델타 탐색 (가로, 세로 방향)
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:                     # 범위 만족시킬 때,

            if not visited[nx][ny] and arr[nx][ny] < h:     # 봉우리 높이가 더 낮으면
                visited[nx][ny] = True                      # 방문 표시
                trail(nx, ny, arr[nx][ny], c + 1)           # 해당 봉우리에서 탐색 GO
                visited[nx][ny] = False                     # 재귀 빠져나오면 방문 표시 해제

            elif not visited[nx][ny] and arr[nx][ny] >= h and not cut:    # 봉우리 높이가 같거나 더 높고 공사 횟수가 남아있을 때,
                if arr[nx][ny] - (h - 1) <= k:                            # 최대 공사를 했을 때 현재 봉우리(h) - 1의 높이가 가능하면
                    visited[nx][ny] = True                                # 방문 표시
                    cut = True                                            # 공사 표시
                    trail(nx, ny, h - 1, c + 1)                           # 해당 봉우리에서 탐색 GO, 다만 높이는 h - 1로 진행함 (가장 최대 등산로를 구할 가능성이 높아짐)
                    visited[nx][ny] = False                               # 재귀 빠져나오면 방문 표시 해제
                    cut = False                                           # 공사 표시도 해제


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_h = 0                               # 가장 높은 봉우리
    max_height = []                         # 시작점을 담을 리스트

    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_h:           # 새로운 최고 높이,
                max_h = arr[i][j]           # 최고 높이 갱신
                max_height = [[i, j]]       # 리스트를 새로 초기화하고 현재 좌표만 담음

            elif arr[i][j] == max_h:        # 최고 높이와 같을 때,
                max_height.append([i, j])   # 시작점만 추가해줌

    max_length = 0
    for x, y in max_height:                             # 각각의 시작점에서 검사
        cut = False                                     # 공사 여부
        visited = [[False] * n for _ in range(n)]       # 지나온 등산로 표시
        visited[x][y] = True                            # 시작점 방문 체크
        trail(x, y, max_h, 1)
    print(f'#{tc} {max_length}')