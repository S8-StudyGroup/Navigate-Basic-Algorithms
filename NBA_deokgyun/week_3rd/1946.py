# 간단한 압축풀기

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    ten_count = 0
    print(f"#{test_count}")
    for _ in range(N):
        Ci, Ki = input().split()
        for _ in range(int(Ki)):
            print(Ci, end="")
            ten_count += 1
            if ten_count % 10 == 0:
                print()
    print()
