# [Programmers] 68645. 삼각 달팽이


def solution(n):
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    answer = [[0] * i for i in range(1, n + 1)]
    goal = n * (n + 1) // 2
    cnt = 2
    x = 0
    y = 0
    answer[x][y] = 1
    while cnt <= goal:
        for d in range(3):
            move_x, move_y = x + dx[d], y + dy[d]
            while (
                0 <= move_x < n
                and 0 <= move_y < len(answer[move_x])
                and answer[move_x][move_y] == 0
            ):
                answer[move_x][move_y] = cnt
                cnt += 1
                x, y = move_x, move_y
                move_x += dx[d]
                move_y += dy[d]

    triangle_snail = []
    for row in answer:
        triangle_snail.extend(row)

    return triangle_snail
