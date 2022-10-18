# [Programmers] 64061. 크레인 인형뽑기 게임


def solution(board, moves):
    answer = 0                                          # 사라진 인형의 개수
    stack = []                                          # 바구니

    for move in moves:                                  # 크레인을 작동시킨 위치의
        for i in range(len(board)):                     # 열 탐색
            if board[i][move - 1] != 0:                 # 인형이 있다면
                pick_up = board[i][move - 1]            # 집어올린다!
                board[i][move - 1] = 0                  # 해당 위치의 인형은 사라진다.
                if stack and stack[-1] == pick_up:      # 같은 인형이 연속해서 쌓이게 되면
                    stack.pop()                         # 두 인형은 터뜨려지면서 바구니에서 사라진다.
                    answer += 2                         # 사라진 인형의 개수 + 2
                else:                                   # 같은 인형이 아니라면
                    stack.append(pick_up)               # 그대로 바구니에 추가
                break                                   # 인형을 들어올렸으므로 더 이상 열을 탐색하지 않고 종료
    return answer
