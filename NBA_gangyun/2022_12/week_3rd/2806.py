# [SWEA] 2806. N-Queen

def dfs(row, col):
    global count
    board[row][col] += 1

    if row == N - 1:
        count += 1
        return

    for i in range(1, N):
        board[i][col] += 1
        board[row][i] += 1
        if row + i < N and col + i < N:
            board[row + i][col + i] += 1
        if row + i < N and col - i >= 0:
            board[row + i][col - i] += 1

    next_row = row + 1
    for next_col in range(N):
        if board[next_row][next_col] == 0:
            dfs(next_row, next_col)
            board[next_row][next_col] -= 1

    for i in range(1, N):
        board[i][col] -= 1
        board[row][i] -= 1
        if row + i < N and col + i < N:
            board[row + i][col + i] -= 1
        if row + i < N and col - i >= 0:
            board[row + i][col - i] -= 1


for test_case in range(1, int(input()) + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        dfs(0, i)
        board = [[0] * N for _ in range(N)]

    print(f'#{test_case} {count}')