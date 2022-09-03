# 백준 - 색종이

board = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for _ in range(int(input())):
    x, y = map(int, input().split())

    # 2차원 좌표를 푸는 관점으로 x, y를 생각!
    for j in range(y, y + 10):
        for i in range(x, x + 10):
            # 이미 검은 영역인 곳은 제외하고 흰 영역만 검게 칠해주며 카운트한다.
            if board[j][i] == 0:
                board[j][i] = 1
                cnt += 1

print(cnt)
