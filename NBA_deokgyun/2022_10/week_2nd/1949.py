# [SWEA] 1949. 등산로 조성

import sys

sys.stdin = open("input.txt")


def sliding_down(x, y, prev_height, depth=1):
    global max_depth
    if not (0 <= x < square and 0 <= y < square):
        return
    if square_list[x][y] >= prev_height and not depth == 1:
        return
    sliding_down(x + 1, y, square_list[x][y], depth + 1)
    sliding_down(x - 1, y, square_list[x][y], depth + 1)
    sliding_down(x, y + 1, square_list[x][y], depth + 1)
    sliding_down(x, y - 1, square_list[x][y], depth + 1)
    if max_depth >= depth:
        return
    max_depth = depth


for test_count in range(1, int(input()) + 1):
    square, dig_depth = map(int, input().split())
    square_list = [list(map(int, input().split())) for _ in range(square)]
    highest_list = []
    highest_value = 0
    for i in range(square):
        for j in range(square):
            if square_list[i][j] > highest_value:
                highest_value = square_list[i][j]
                highest_list = []
                highest_list.append((i, j))
            elif square_list[i][j] == highest_value:
                highest_list.append((i, j))
    max_depth = 0
    for i in range(square):
        for j in range(square):
            for k in range(dig_depth + 1):
                square_list[i][j] -= k
                for a, b in highest_list:
                    sliding_down(a, b, square_list[a][b])
                square_list[i][j] += k
    print(f"#{test_count}", max_depth)
