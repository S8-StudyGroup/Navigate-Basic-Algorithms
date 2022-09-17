# [BOJ] 색종이
# Guest - 김영주 교수님

paper = [[0] * 100 for _ in range(100)]

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            # 색종이에 대해 도화지에 칠한다.
            paper[i][j] = 1

# 도화지에서 1인 것만 다 더해요
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]

# total = sum([sum(line) for line in paper])
# total = sum(map(sum, paper))
print(total)
