# [BOJ] 15683. 감시

from itertools import product
from copy import deepcopy

# 상 우 하 좌
di = [-1, 0, 1, 0, -1, 0, 1, 0]
dj = [0, 1, 0, -1, 0, 1, 0, -1]

cctv = {1: [1], 2: [3, 1], 3: [0, 1], 4: [3, 0, 1], 5: [0, 1, 2, 3]}

row, col = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(row)]
cctv_points = []
min_count = row * col

for i in range(row):
    for j in range(col):
        if 0 < office[i][j] < 6:
            cctv_points.append((i, j))

cctv_nums = len(cctv_points)

for comb in product([0, 1, 2, 3], repeat=cctv_nums):
    print(comb)
    new_office = deepcopy(office)
    count = 0
    for cctv_num in range(cctv_nums):
        cctv_i = cctv_points[cctv_num][0]
        cctv_j = cctv_points[cctv_num][1]
        for direction in cctv[new_office[cctv_i][cctv_j]]:
            k = 1
            check_i = cctv_i + k * di[direction + comb[cctv_num]]
            check_j = cctv_j + k * dj[direction + comb[cctv_num]]
            while 0 <= check_i < row and 0 <= check_j < col:
                if new_office[check_i][check_j] == 0 or new_office[check_i][check_j] == 7:
                    new_office[check_i][check_j] = 7
                elif new_office[check_i][check_j] == 6:
                    break
                k += 1
                check_i = cctv_i + k * di[direction + comb[cctv_num]]
                check_j = cctv_j + k * dj[direction + comb[cctv_num]]

    for i in range(row):
        for j in range(col):
            if new_office[i][j] == 0:
                count += 1

    if count < min_count:
        min_count = count

print(min_count)


