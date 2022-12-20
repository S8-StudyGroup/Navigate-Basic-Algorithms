# [SWEA] 2806. N-Queen

# 델타 탐색(8방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
 
 
def dfs(depth):
    if depth == N:
        global cnt
        cnt += 1
        return
 
    for i in range(N):
        if matrix[depth][i] == 0:                               # 해당 자리가 비었다면
            matrix[depth][i] = 2                                # 퀸 위치로 설정
            change_list = []                                    # dfs 후 복구시켜줄 위치 리스트

            for d in range(8):                                  # 퀸이 공격할 수 있는 위치 선별
                move_x, move_y = depth + dx[d], i + dy[d]
                while 0 <= move_x < N and 0 <= move_y < N:
                    if matrix[move_x][move_y] == 0:
                        matrix[move_x][move_y] = 1
                        change_list.append((move_x, move_y))
                    move_x += dx[d]
                    move_y += dy[d]

            dfs(depth + 1)                                      # 다음 행으로 dfs

            for move_x, move_y in change_list:                  # 원상 복구
                matrix[move_x][move_y] = 0
            matrix[depth][i] = 0
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    cnt = 0
    dfs(0)                                  # 0번째 행부터 dfs 진행
 
    print(f"#{tc} {cnt}")