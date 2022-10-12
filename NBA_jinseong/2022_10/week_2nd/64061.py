# [Programmers] 64061. 크레인 인형뽑기 게임

# idea
# 1. 인형 고르기
# 위치(j)마다 맨 위부터 0이 아닐 때까지 내려감(i를 0부터)
# 0이 아니면 옆으로 옮기기
# 2. 인형 2개면 없애기
# 바구니에 담긴 인형 2개가 연속된 숫자면 없애기

def solution(board, moves):
    answer = 0
    cnt = 0
    basket = [0] * 1000

    for move in moves:
        j = move - 1
        for i in range(len(board)):
            if board[i][j]:                             # 해당 위치의 맨 위의 인형 발견
                doll = board[i][j]
                board[i][j] = 0
                basket[cnt] = doll                      # 바구니에 인형 담기
                cnt += 1                                # 인형 개수 추가

                if cnt >= 2:
                    if basket[cnt-1] == basket[cnt-2]:  # 같은 인형이 연속되면
                        basket.pop()                    # 인형 두개 없애고
                        basket.pop()
                        cnt -= 2                        # 담긴 인형수 2개 줄이기
                        answer += 2
                break                                   # 인형하나 찾았으니깐 다음 move
    return answer

