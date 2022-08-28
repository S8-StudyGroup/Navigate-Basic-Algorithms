# 백준 - 색종이

board = [[0] * 100 for _ in range(100)]

paper = int(input())

for _ in range(paper):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            board[x + i][y + j] = 1

result = 0

for i in range(100):
    result += sum(board[i])

print(result)
