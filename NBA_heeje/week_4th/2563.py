# 백준 - 색종이

board = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for _ in range(int(input())):
    x, y = map(int, input().split())

    for j in range(y, y + 10):
        for i in range(x, x + 10):
            if board[j][i] == 0:
                board[j][i] = 1
                cnt += 1

print(cnt)
