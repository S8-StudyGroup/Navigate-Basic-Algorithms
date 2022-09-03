# 백준 - 색종이

import sys

sys.stdin = open("input.txt")


def how_many_1s(x: int, y: int) -> int:
    count_new_1s = 0
    for i in range(10):
        for j in range(10):
            if white_paper[x - i][y + j] != 1:
                white_paper[x - i][y + j] = 1
                count_new_1s += 1
    return count_new_1s


color_paper_count: int = int(input())

white_paper = [[0] * 100 for _ in range(100)]
result = 0
for _ in range(color_paper_count):
    idx_x, idx_y = map(int, input().split())
    result += how_many_1s(idx_x, idx_y)

print(result)
