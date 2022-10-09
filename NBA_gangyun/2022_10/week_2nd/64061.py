# [Programmers] 64061. 크레인 인형뽑기 게임

def solution(board, moves):
    size = len(board)
    basket = [0]
    disappeared = 0
    for j in moves:
        pick = 0
        for i in range(size):
            if board[i][j - 1] != 0:
                pick = board[i][j - 1]
                board[i][j - 1] = 0
                break

        if pick != 0:
            if pick != basket[-1]:
                basket.append(pick)
            else:
                basket.pop()
                disappeared += 2

    answer = disappeared
    return answer


# print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
