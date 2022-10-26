# [Programmers] 68645. 삼각 달팽이


move = [[1, 0], [0, 1], [-1, -1]]


def solution(n):
    board = [[0] * n for _ in range(n)]

    status = 0  # 0: 아래로, 1: 오른쪽, 2: 위쪽
    x, y = 0, 0
    for i in range(n * (n + 1) // 2):
        board[x][y] = i + 1
        dx, dy = move[status]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (board[nx][ny] != 0):
            status = (status + 1) % 3
            dx, dy = move[status]
            nx, ny = x + dx, y + dy

        x, y = nx, ny

    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(board[i][j])

    return answer
