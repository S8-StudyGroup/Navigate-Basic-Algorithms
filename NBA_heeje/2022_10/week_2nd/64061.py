# [Programmers] 64061. 크레인 인형뽑기 게임


def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                pick_up = board[i][move - 1]
                board[i][move - 1] = 0
                if stack and stack[-1] == pick_up:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(pick_up)
                break
    return answer
