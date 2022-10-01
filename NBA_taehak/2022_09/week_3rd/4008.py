# [SWEA] 4008. 숫자 만들기
import sys

sys.stdin = open('4008.txt')


def my_cal(idx, memo, plus, minus, multi, divi):

    global my_min, my_max, idx_end

    if idx == idx_end:
        if my_max < memo:
            my_max = memo
        if my_min > memo:
            my_min = memo
        return

    if plus > 0:
        my_cal(idx + 1, memo + nums[idx], plus - 1, minus, multi, divi)

    if minus > 0:
        my_cal(idx + 1, memo - nums[idx], plus, minus - 1, multi, divi)

    if multi > 0:
        my_cal(idx + 1, memo * nums[idx], plus, minus, multi - 1, divi)

    if divi > 0:
        my_cal(idx + 1, int(memo / nums[idx]), plus, minus, multi, divi - 1)


for case in range(1, int(input()) + 1):
    idx_end = int(input())
    plus, minus, multi, divi = map(int, input().split())
    nums = list(map(int, input().split()))

    my_min = 10**8
    my_max = -my_min

    my_cal(1, nums[0], plus, minus, multi, divi)
    print(f'#{case} {my_max - my_min}')
