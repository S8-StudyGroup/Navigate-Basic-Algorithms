# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

import sys
from collections import deque

sys.stdin = open('input.txt')


def merge_sort(m):
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(deque(left), deque(right))


def merge(l, r):
    global cnt
    result = []

    if l[-1] > r[-1]:
        cnt += 1

    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                result.append(l.popleft())
            else:
                result.append(r.popleft())
        elif len(l) > 0:
            result.append(l.popleft())
        elif len(r) > 0:
            result.append(r.popleft())

    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    sorted_list = merge_sort(numbers)

    print(f"#{tc} {sorted_list[N // 2]} {cnt}")
