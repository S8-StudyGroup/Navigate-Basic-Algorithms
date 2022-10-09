# 1949. [모의 SW 역량테스트] 등산로 조성

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, cur_cnt, is_built):
    is_done = True
    for d in range(4):
        move_x, move_y = x + dx[d], y + dy[d]
        if 0 <= move_x < N and 0 <= move_y < N and not visited[move_x][move_y]:
            if matrix[x][y] > matrix[move_x][move_y]:
                visited[move_x][move_y] = True
                dfs(move_x, move_y, cur_cnt + 1, is_built)
                visited[move_x][move_y] = False
                is_done = False

            elif not is_built and matrix[x][y] > matrix[move_x][move_y] - K:
                temp = matrix[move_x][move_y]
                matrix[move_x][move_y] = matrix[x][y] - 1
                visited[move_x][move_y] = True
                dfs(move_x, move_y, cur_cnt + 1, True)
                visited[move_x][move_y] = False
                matrix[move_x][move_y] = temp
                is_done = False

    if is_done:
        global max_cnt
        if max_cnt < cur_cnt:
            max_cnt = cur_cnt


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    peaks = []
    max_cnt = 0
    max_peak = 0
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] > max_peak:
                max_peak = row[j]
                peaks = [(i, j)]
            elif row[j] == max_peak:
                peaks.append((i, j))
        matrix.append(row)

    visited = [[False] * N for _ in range(N)]
    for peak in peaks:
        visited[peak[0]][peak[1]] = True
        dfs(*peak, 1, False)
        visited[peak[0]][peak[1]] = False

    print(f"#{tc} {max_cnt}")
