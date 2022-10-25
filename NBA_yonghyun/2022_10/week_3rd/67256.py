# [Programmers] 67256. 키패드 누르기


left_num = [1, 4, 7]
right_num = [3, 6, 9]

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
    0: [3, 1],
}


def solution(numbers, hand):  # 핵심은 현재 손가락 위치 갱신!!
    left = [3, 0]
    right = [3, 2]
    answer = ''

    for num in numbers:
        if num in left_num:  # 왼쪽 숫자
            answer += 'L'
            left = keypad[num]

        elif num in right_num:  # 오른쪽 숫자
            answer += 'R'
            right = keypad[num]

        else:  # 키패드 이동거리 구하기
            left_dis = abs(keypad[num][0] - left[0]) + abs(keypad[num][1] - left[1])
            right_dis = abs(keypad[num][0] - right[0]) + abs(keypad[num][1] - right[1])

            if left_dis == right_dis:  # 거리가 같으면
                answer += hand[0].upper()
                if hand == "left":
                    left = keypad[num]
                else:
                    right = keypad[num]
            elif left_dis > right_dis:  # 오른손이 더 가까움
                answer += 'R'
                right = keypad[num]
            elif left_dis < right_dis:  # 왼손이 더 가까움
                answer += 'L'
                left = keypad[num]

    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
