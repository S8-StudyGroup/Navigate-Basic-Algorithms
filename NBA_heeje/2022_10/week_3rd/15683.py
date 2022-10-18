# [BOJ] 15683. 감시

# 각 cctv의 감시 구역 (key: CCTV번호, value: 감시 방향)
cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

# 델타 탐색
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(idx, cnt_blind_spot):                       # idx: cctv_list의 idx / cnt_blindspot: 사각지대 개수
    if idx == len_cctv_list:                        # 모든 cctv를 탐색했다면
        global min_cnt_blind_spot
        if min_cnt_blind_spot > cnt_blind_spot:     # 현재 사각지대와 최소 사각지대의 개수 비교
            min_cnt_blind_spot = cnt_blind_spot
        return

    x, y = cctv_list[idx]
    for d_list in cctv_dir[matrix[x][y]]:           # 현재 cctv의 감시 가능 방향만 탐색
        change_list = []                            # 재귀 후 복구시켜줘야 할 위치 저장
        for d in d_list:
            move_x, move_y = x + dx[d], y + dy[d]

            # 해당 위치가 유효성 검사를 통과하고 벽이 아닌 경우
            while 0 <= move_x < N and 0 <= move_y < M and matrix[move_x][move_y] != 6:
                if matrix[move_x][move_y] == 0:                # 빈 칸이라면
                    matrix[move_x][move_y] = 7                 # 감시 구역으로 설정
                    change_list.append((move_x, move_y))       # 해당 위치 저장
                    cnt_blind_spot -= 1                        # 사각지대 개수 - 1
                move_x += dx[d]                                # 다음 위치로 이동
                move_y += dy[d]

        dfs(idx + 1, cnt_blind_spot)                           # 다음 cctv 탐색

        for move_x, move_y in change_list:                     # 재귀 후 원상태로 복구해주는 작업
            matrix[move_x][move_y] = 0
            cnt_blind_spot += 1


N, M = map(int, input().split())
matrix = []
cctv_list = []
min_cnt_blind_spot = N * M
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 5:                    # cctv는 cctv_list에 따로 저장
            cctv_list.append((i, j))
            min_cnt_blind_spot -= 1
        elif row[j] == 6:                       # 벽은 사각지대가 아니므로 총 사각지대 개수 - 1
            min_cnt_blind_spot -= 1
    matrix.append(row)

len_cctv_list = len(cctv_list)
dfs(0, min_cnt_blind_spot)

print(min_cnt_blind_spot)
