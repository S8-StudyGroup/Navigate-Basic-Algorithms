# [Programmers] 67256. 키패드 누르기

# [Programmers] 67256. 키패드 누르기


# 1, 4, 7 왼손
# 3, 6, 9 오른쪽
# 2, 5, 8, 0은 가까운 걸루
# 상하좌우만 이동 가능

# idea
# 누를 숫자 받기
# 현재 왼손과 오른손과의 거리 구하기
# -> 좌표차로 금방 구하기
# 그리고 비교하기
# 같으면 hand에 저장된 손으로 하기

keypad = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    '*': [3, 0],
    0: [3, 1],
    '#': [3, 2],
}


def solution(numbers, hand):
    answer = ''

    left_hand = keypad['*']             # 왼손
    right_hand = keypad['#']            # 오른손

    for number in numbers:              # 누를 번호 받기
        distance_left = 0               # 왼손위치와 누를 번호 거리
        distance_right = 0              # 오른손위치와 누를 번호 거리
        pushing_number = keypad[number] # 누를 번호 위치

        if number in [1, 4, 7]:         # 왼열
            answer = answer + 'L'
            left_hand = pushing_number  # 왼손 이동
        elif number in [3, 6, 9]:       # 오른열
            answer = answer + 'R'
            right_hand = pushing_number     # 오른손 이동
        elif number in [2, 5, 8, 0]:        # 가운데 열
            for i in range(2):              # 각 손의 거리 계산
                distance_left += abs(pushing_number[i] - left_hand[i])
                distance_right += abs(pushing_number[i] - right_hand[i])

            if distance_left > distance_right:      # 오른손이 가까우면
                answer = answer + 'R'               # 누르는 데 추가
                right_hand = pushing_number         # 오른손 이동
            elif distance_left < distance_right:    # 왼손이 가까우면
                answer = answer + 'L'
                left_hand = pushing_number          # 왼손 이동
            else:                                   # 거리가 같으면
                if hand == 'left':                  # 왼손잡이면
                    answer = answer + 'L'
                    left_hand = pushing_number      # 왼손 이동
                elif hand == 'right':               # 오른손잡이면
                    answer = answer + 'R'           # 누르는 데 추가
                    right_hand = pushing_number     # 오른손 이동

    return answer


