# [SWEA] 2806. N-Queen

# 상 우상 우 우하 하 좌하 좌 좌상
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def check_queen(i, j):
    for direction in range(8):
        for k in range(N):
            check_i = i + di[direction] * k
            check_j = j + dj[direction] * k
            if 0 <= check_i < N and 0 <= check_j < N and board[check_i][check_j] == 0:
                board[check_i][check_j] = 1


for test_case in range(1, int(input()) + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    print(board)
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                board[row][col] = 2
                check_queen(row, col)
                print(board)