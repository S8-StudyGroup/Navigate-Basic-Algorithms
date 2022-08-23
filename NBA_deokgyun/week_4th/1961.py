# 숫자 배열 회전

import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    n_list_lotate_90 = list(zip(*n_list[::-1]))
    n_list_lotate_180 = list(zip(*n_list_lotate_90[::-1]))
    n_list_lotate_270 = list(zip(*n_list_lotate_180[::-1]))
    print("#{}".format(test_count))
    for i in range(n):
        print(*n_list_lotate_90[i], sep="", end=" ")
        print(*n_list_lotate_180[i], sep="", end=" ")
        print(*n_list_lotate_270[i], sep="")
