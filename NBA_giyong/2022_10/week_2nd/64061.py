# [Programmers] 64061. 크레인 인형뽑기 게임
def solution(board, moves):
    n = len(board)                                  # 깊이를 알기위해 n 값을 지정
    basket = []                                     # 바구니 만들어준다
    answer = 0                                      # 사라진 인형의 개수
    for move in moves:                              # 인형을 뺄 위치 
        for i in range(n):                          # 깊이를 탐색해준다
            if board[i][move - 1] != 0:             # 있다면
                basket.append(board[i][move - 1])   # 바구니에 넣어주고
                board[i][move - 1] = 0              # 값을 0으로 해준다(나갔으니)
                
                if len(basket) > 1:                 # 바구니의 값이 한개 이상일때
                    if basket[-1] == basket[-2]:    # 맨마지막꺼랑 그 마지막 꺼 다음꺼랑 같다면
                        basket.pop()                # 마지막꺼 두개를 빼준다
                        basket.pop()
                        answer += 2                 # 사라진 인형의 개수는 두개씩이므로 2를 더해준다
                break
    return answer