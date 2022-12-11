# [Programmers] 77485. 행렬 테두리 회전하기

def solution(rows, columns, queries):
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    board = [[] for _ in range(rows)]
    answer = []
    for i in range(rows):
        for j in range(1, columns + 1):
            board[i].append(i * columns + j)

    for point in queries:
        direction = 0
        start_i, start_j = point[0] - 1, point[1] - 1
        now_board = board[start_i][start_j]
        board[start_i][start_j] = board[start_i + 1][start_j]
        new_list = [board[start_i][start_j]]
        while not(start_i == point[0] and start_j == point[1] - 1):
            if start_i == point[0] - 1 and start_j == point[3] - 1:
                direction = 1
            elif start_i == point[2] - 1 and start_j == point[3] - 1:
                direction = 2
            elif start_i == point[2] - 1 and start_j == point[1] - 1:
                direction = 3
            start_i += di[direction]
            start_j += dj[direction]
            next_board = board[start_i][start_j]
            board[start_i][start_j] = now_board
            new_list.append(now_board)
            now_board = next_board
        answer.append(min(new_list))
    return answer
