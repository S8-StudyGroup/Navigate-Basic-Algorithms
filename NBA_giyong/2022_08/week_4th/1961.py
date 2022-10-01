# 숫자 배열 회전
import sys

sys.stdin = open("input")


def turn_arr(a, n):
    b = [[0] * n for _ in range(n)]
    for s in range(n):
        for d in range(n):
            b[d][n-1-s] = a[s][d]
    return b


t = int(input())

for tc in range(1, t + 1):
    c = int(input())
    print(f'#{tc}')
    arr = [list(map(int, input().split())) for _ in range(c)]

    arr_90 = turn_arr(arr, c)
    arr_180 = turn_arr(arr_90, c)
    arr_270 = turn_arr(arr_180, c)

    for i in range(c):
        for x in range(c):
            print(arr_90[i][x], end='')
        print(end=' ')
        for y in range(c):
            print(arr_180[i][y], end='')
        print(end=' ')
        for z in range(c):
            print(arr_270[i][z], end='')
        print()