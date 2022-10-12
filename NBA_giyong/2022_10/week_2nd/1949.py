# [SWEA] 1949. 등산로 조성
import sys

sys.stdin = open("input.txt")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(row, col, road, con):  # 좌표랑 길 공사현황
    global max_value

    if road > max_value:            # 길의 최대값을 찾으면 갱신
        max_value = road

    visited[row][col] = 1           # 방문표시

    for d in range(4):              # 델타탐색
        nx = row + dx[d]
        ny = col + dy[d]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:         # 범위안에 있거나 방문하지 않았으면
            if arr[row][col] > arr[nx][ny]:                             # 만일 내가 다른 봉우리 보다 크면
                dfs(nx, ny, road + 1, con)                              # 재귀로 다시 탐색해준다
            elif con and arr[nx][ny] - k < arr[row][col]:               # 만일 현 위치보다 높거나 같은 곳으로 이동할때
                temp = arr[nx][ny]                                      # 기록
                arr[nx][ny] = arr[row][col] - 1                         # 공사하기
                dfs(nx, ny, road + 1, 0)                                # 재귀로 다시 탐색
                arr[nx][ny] = temp                                      # 원상복구

    visited[row][col] = 0           # 다른 봉우리를 탐색하기 위해서 원상복구


t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_heigth = 0                         # 최고 봉우리 값을 저장할 변수

    for i in range(n):                      # 최고 봉우리의 값을 찾는다
        for j in range(n):
            if max_heigth < arr[i][j]:
                max_heigth = arr[i][j]

    max_value = 0
    visited = [[0] * n for _ in range(n)]  # 방문했는지 확인하기위한 방문자 리스트
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_heigth:
                dfs(i, j, 1, 1)

    print(f'#{tc} {max_value}')