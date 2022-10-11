# [Programmers] 64061. 크레인 인형뽑기 게임


def solution(board, moves):
    answer = []
    answer_cnt = 0
    b_size = len(board)
    for k in moves:
        for i in range(b_size):
            if board[i][k - 1]:
                if answer == [] or answer[-1] != board[i][k - 1]:
                    answer.append(board[i][k - 1])
                elif answer[-1] == board[i][k - 1]:
                    answer.pop()
                    answer_cnt += 2
                board[i][k - 1] = 0
                break
    return answer_cnt
