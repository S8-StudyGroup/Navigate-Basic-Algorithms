# 백준 - 색종이

board = [[0] * 100 for _ in range(100)]  # 흰 도화지 board

num = int(input())

cnt = 0  # 검은색 칸 수

for paper in range(num):  # 색종이 개수마다
    a, b = map(int, input().split())  # 색종이의 왼쪽 상단, 오른쪽 하단 위치를 받음

    for i in range(100 - b - 10, 100 - b):
        for j in range(a, a + 10):
            if board[i][j] == 0:  # 이미 검은색으로 겹쳐진 부분은 무시하고 겹쳐지지 않은 범위를
                board[i][j] = 1  # 1로 표시해준 후
                cnt += 1  # 한 칸을 + 1

print(cnt)
