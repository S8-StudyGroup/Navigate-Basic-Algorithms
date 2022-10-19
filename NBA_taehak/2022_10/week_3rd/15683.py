# [BOJ] 15683. 감시
import copy
import sys
input = sys.stdin.readline

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

modes = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]],
}

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if area[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([area[i][j], i, j])


def fill(board, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7


def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in modes[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = 999999999
dfs(0, area)
print(min_value)