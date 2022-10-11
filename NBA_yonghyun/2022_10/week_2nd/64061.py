# [Programmers] 64061. 크레인 인형뽑기 게임



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    n = len(board)
    basket = [0]
    answer = 0

    for turn in moves:
        for i in range(n):
            if board[i][turn - 1] != 0:
                # print(board[i][turn - 1])
                basket.append(board[i][turn - 1])
                board[i][turn - 1] = 0
                # print(turn, basket)
                if basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
    return answer


print(solution(board, moves))
