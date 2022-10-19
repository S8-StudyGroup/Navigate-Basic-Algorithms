# [Programmers] 67256. 키패드 누르기
def solution(numbers, hand):
    key_pad = {                             # 키패드 딕셔너리
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }

    left_hand = [1, 4, 7]           # 왼손이면 누르는 숫자 리스트
    right_hand = [3, 6, 9]          # 오른손이면 누르는 숫자 리스트

    result = []

    left_start = key_pad['*']       # 왼손 시작우치
    right_start = key_pad['#']      # 오른손 시작위치
    for number in numbers:
        now = key_pad[number]       # 현재위치
        if number in left_hand:     # 숫자가 왼손리스트에 있으면
            result.append('L')      # 빈리스트에 넣어준다
            left_start = now        # 왼손의 위치를 현재위치로 변경
        elif number in right_hand:  # 숫자가 오른손리스트에 있으면
            result.append('R')
            right_start = now       # 오른손의 위치를 현재위치로 변경

        else:
            left_d = 0  # 왼쪽거리
            right_d = 0   # 오른쪽 거리

            for a, b, c in zip(left_start, right_start, now):
                left_d += abs(a - c)        # 왼쪽손과 현재의 거리
                right_d += abs(b - c)       # 오른손과 현재의 거리

            if left_d < right_d:            # 오른손이 크면 왼손이 가까우니까
                result.append('L')
                left_start = now            # 왼손위치를 현재로 바꿈

            elif left_d > right_d:          # 왼손이 크면 오른손이 가까움으로 오른손 추가
                result.append('R')
                right_start = now

            else:                           # 왼손과 오른손의 거리가 같다면
                if hand == 'right':         # 오른손인지 확인
                    result.append('R')
                    right_start = now
                else:                       # 왼손인지 확인
                    result.append('L')
                    left_start = now

    answer = ''.join(result)

    return answer

#
# arr = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# arr1 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# a = 'right'
# b = 'left'
# solution(arr, a)
# solution(arr1, b)
# solution(arr2, a)
