# [BOJ] 2638. 치즈

import sys
from copy import deepcopy
input = sys.stdin.readline


def inner_check(grid):
    checked_grid = deepcopy(grid)
    for i in range(row):
        for j in range(col):
            if checked_grid[i][j] == 0:
                inner_count = 0
                for direction in range(4):
                    for k in range(1, max(row, col)):
                        check_i = i + di[direction] * k
                        check_j = j + dj[direction] * k
                        if 0 <= check_i < row and 0 <= check_j < col and checked_grid[check_i][check_j] == 1:
                            inner_count += 1
                            break
                if inner_count == 4:
                    checked_grid[i][j] = 2

    return checked_grid


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

row, col = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(row)]
result = 0
escape_counter = 0

for i in range(row):
    for j in range(col):
        if grid[i][j] == 1:
            escape_counter += 1
            break

while escape_counter != 0:
    inner_checked_grid = inner_check(grid)
    for i in range(row):
        for j in range(col):
            if inner_checked_grid[i][j] == 1:
                melt_count = 0
                for direction in range(4):
                    check_i = i + di[direction]
                    check_j = j + dj[direction]
                    if inner_checked_grid[check_i][check_j] == 0:
                        melt_count += 1
                    if melt_count >= 2:
                        grid[i][j] = 0
                        break

    result += 1
    escape_counter = 0

    # 치즈가 녹은 후에도 남아있으면 반복문 탈출
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                escape_counter += 1
                break

print(result)