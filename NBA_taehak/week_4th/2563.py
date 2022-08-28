# 백준 - 색종이

# 도화지 100 * 100
# 색종이 10 * 10
# 2차원 리스트 100 * 100 만들고 색종이 붙이는 부분을 1로 바꾸기

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