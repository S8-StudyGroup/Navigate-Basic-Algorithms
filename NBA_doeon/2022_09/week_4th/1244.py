# 1244. 최대 상금

def get_prize(cnt):
    global max_prize    # 최대 상금
    global is_final     # 최대값임을 보장, 이 경우 모든 재귀에서 빠져나올 수 있도록 함

    if is_final == False:   # 이전에서 최대값 보장 받았으면 모든 재귀에서 빠져나옴
        if cards == max_case and (turns - cnt) % 2 == 0:    # 만들어진 순열이 이미 최대값이고 남은 교환 횟수가 짝수
            prize = ''.join(cards)
            max_prize = int(prize)                          # max_prize를 정해주고
            is_final = True                                 # 최대값 보장하는 is_final을 True
            return
    
        if len(set(cards)) == len(cards) and cards == max_case and (turns - cnt) % 2 == 1:  # 중복되는 숫자 없고, 순열이 이미 최대값, 남은 교환 횟수가 홀수
            cards[-1], cards[-2] = cards[-2], cards[-1]                                     # 마지막 두 개의 위치만 바꿔주고
            prize = ''.join(cards)
            max_prize = int(prize)                                                          # max_prize로 확정 후
            is_final = True                                                                 # 최대값 보장
            return
    
        if cnt == turns:                # 교환 횟수를 다 쓴 경우 -> 종료
            prize = ''.join(cards)      # cards 원소를 붙여서 상금으로 변환하고
            if int(prize) > max_prize:  # 최대 상금보다 현재 상금이 크다면
                max_prize = int(prize)  # 최대 상금 갱신
            return
    
        else:                           # 교환 횟수가 남은 경우
            for i in range(len(cards) - 1):                 # 교환할 왼쪽 카드 인덱스
                for j in range(i + 1, len(cards)):          # 교환할 오른쪽 카드 인덱스
                    cards[i], cards[j] = cards[j], cards[i]
                    get_prize(cnt + 1)                      # 교환된 cards 값을 그대로 가지고 다음 turn 교환 횟수로 감
                    cards[i], cards[j] = cards[j], cards[i] # return해오면 바꾼 cards 위치를 원상복구


t = int(input())
for tc in range(1, t + 1):
    card, n = input().split()

    cards = list(card)                      # cards 리스트
    turns = int(n)                          # 교환 횟수
    max_case = sorted(cards, reverse=True)  # cards를 내림차순한 리스트(만들어질 수 있는 최대값)

    max_prize = 0                           # 초기 최대 상금
    is_final = False                        # 최대값 보장하는 변수

    get_prize(0)                            # 현재 교환한 횟수 0으로 함수 실행

    print(f'#{tc} {max_prize}')
