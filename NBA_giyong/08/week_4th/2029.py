# 몫과 나머지 출력하기

import sys

sys.stdin = open("input")

t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    share = a // b
    remainder = a % b

    print(f"#{tc}", end=" ")
    print(share, remainder)