# [Programmers] 87694. 아이템 줍기

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j, my_direction):
    if board[i][j] == 0 or board[i][j] == 2:
        return

    board[i][j] = 2

    for direction in range(4):
        next_i = i + di[direction]
        next_j = j + dj[direction]
        if 0 <= next_i < 20 and 0 <= next_j < 20 and board[next_i][next_j] == 1:
            corner_check_i = next_i + di[(4 + direction - 1) % 4]
            corner_check_j = next_j + dj[(4 + direction - 1) % 4]
            if board[corner_check_i][corner_check_j] == 0:
                dfs(next_i, next_j, direction)
            else:
                dfs(next_i, next_j, direction)
                board[next_i][next_j] = 1



    # for direction in range(4):
    #     next_i = i + di[direction]
    #     next_j = j + dj[direction]
    #     if 0 <= next_i < 20 and 0 <= next_j < 20:
    #         dfs(next_i, next_j, direction)


def solution(rectangle, characterX, characterY, itemX, itemY):
    global board
    board = [[0] * 20 for _ in range(20)]
    for square in rectangle:
        for row in range(2 * square[1], 2 * square[3]):
            for col in range(2 * square[0], 2 * square[2]):
                board[row][col] = 1

    dfs(2 * characterY, 2 * characterX, 1)

    return board


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))