# 어디에 단어가 들어갈 수 있을까

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    board = []
    total_cnt = 0
    for _ in range(N):
        board.append(list(map(int, input().split())) + [0])

    board.append([0] * (N + 1))
    for i in range(N + 1):
        row_cnt = 0
        col_cnt = 0
        for j in range(N + 1):
            if board[i][j] == 1:
                row_cnt += 1
            else:
                if row_cnt == K:
                    total_cnt += 1
                row_cnt = 0

            if board[j][i] == 1:
                col_cnt += 1
            else:
                if col_cnt == K:
                    total_cnt += 1
                col_cnt = 0

    print(f'#{test_case} {total_cnt}')
