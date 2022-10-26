# [Programmers] 68645. 삼각 달팽이
dx = [1, 0, -1]  # 하 우 왼쪽대각선
dy = [0, 1, -1]


def solution(n):
    arr = [[0] * n for _ in range(n)]
    answer = []
    x, y = 0, 0                                 # 출발위치
    direction = 0                               # 처음 할 방향 아래
    for i in range(1, (n * (n + 1) // 2) + 1):         # 1부터 마지막 수까지 반복
        arr[x][y] = i

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 3
            x += dx[direction]
            y += dy[direction]
    for j in range(n):
        for k in range(n):
            if arr[j][k] != 0:
                answer.append(arr[j][k])
    return answer