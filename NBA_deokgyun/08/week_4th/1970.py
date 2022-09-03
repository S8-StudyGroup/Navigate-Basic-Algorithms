# 쉬운 거스름돈

import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    n = int(input())
    change_cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f"#{test_count}")
    for i in change_cash:
        print(n // i, end=" ")
        n = n % i
    print()
