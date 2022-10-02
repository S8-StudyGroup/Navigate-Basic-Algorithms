# 핀볼 게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&

import sys

sys.stdin = open("sample_input.txt", encoding="utf-8")


def wormhole(hole_num, row, col):
    idx = warmhole_list[hole_num - 6].index((row, col))
    return warmhole_list[hole_num - 6][idx - 1]


def ball_move(row, col, row_move, col_move):
    start_row = row
    start_col = col
    score_count = 0
    while True:
        while not board_list[row][col]:
            row += row_move
            col += col_move
            if not (0 <= row < board_length):
                row -= row_move
                row_move = -row_move
                score_count += 1
            if not (0 <= col < board_length):
                col -= col_move
                col_move = -col_move
                score_count += 1
            if row == start_row and col == start_col:
                return score_count
        if board_list[row][col] == -1:
            return score_count
        elif board_list[row][col] > 5:
            row, col = wormhole(board_list[row][col], row, col)
        elif board_list[row][col] == 1 and (row_move == 1 or col_move == -1):
            row_move, col_move = col_move, row_move
        elif board_list[row][col] == 2 and (row_move == -1 or col_move == -1):
            row_move, col_move = -col_move, -row_move
        elif board_list[row][col] == 3 and (row_move == -1 or col_move == 1):
            row_move, col_move = col_move, row_move
        elif board_list[row][col] == 4 and (row_move == 1 or col_move == 1):
            row_move, col_move = -col_move, -row_move
        else:
            row_move = -row_move
            col_move = -col_move
        if board_list[row][col] < 6:
            score_count += 1
        row += row_move
        col += col_move
        if not (0 <= row < board_length):
            row -= row_move
            row_move = -row_move
            score_count += 1
        if not (0 <= col < board_length):
            col -= col_move
            col_move = -col_move
            score_count += 1
        if row == start_row and col == start_col:
            return score_count


drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]
for test_count in range(1, int(input()) + 1):
    board_length = int(input())
    board_list = [list(map(int, input().split())) for _ in range(board_length)]
    warmhole_list = [[] for _ in range(5)]
    result = 0
    local_result1 = 0
    local_result2 = 0
    for i in range(board_length):
        for j in range(board_length):
            if board_list[i][j] > 5:
                warmhole_list[board_list[i][j] - 6].append((i, j))
    for u in range(board_length):
        for v in range(board_length):
            if board_list[u][v] == 0:
                for k in range(-1, 2, 2):
                    local_result1 = ball_move(u, v, k, 0)
                    local_result2 = ball_move(u, v, 0, k)
                    if local_result1 > result or local_result2 > result:
                        result = local_result1 if local_result1 > local_result2 else local_result2
    print(f"#{test_count}", result)
