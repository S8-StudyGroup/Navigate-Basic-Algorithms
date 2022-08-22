# 백준 - 색종이

base_paper = [[0] * 100 for _ in range(100)]

N = int(input())
start_point = [list(map(int, input().split())) for _ in range(N)]
count = 0

for x, y in start_point:
    for i in range(10):
        for j in range(10):
            base_paper[x + i][y + j] += 1

for i in range(100):
    for j in range(100):
        if base_paper[i][j] > 0:
            count += 1

print(count)