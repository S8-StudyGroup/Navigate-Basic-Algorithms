# 백준 - 색종이
import sys

sys.stdin = open('input')


paper = int(input())  # 색종이의 수
n = 100

arr = [[0] * n for _ in range(n)]
count = 0
for _ in range(paper):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if arr[i][j] != 1:
                arr[i][j] = 1
                count += 1

print(count)