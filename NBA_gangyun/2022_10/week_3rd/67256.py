# [Programmers] 67256. 키패드 누르기

# 상, 우, 하, 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def solution(numbers, hand):
    answer = ''
    left_side = {1: (1, 1), 4: (2, 1), 7: (3, 1)}
    right_side = {3: (1, 3), 6: (2, 3), 9: (3, 3)}
    middle_side = {2: (1, 2), 5: (2, 2), 8: (3, 2), 0: (4, 2)}
    left_location = (4, 1)
    right_location = (4, 3)
    for i in range(len(numbers)):
        if numbers[i] in left_side.keys():
            left_location = left_side[numbers[i]]
            answer += 'L'
        elif numbers[i] in right_side.keys():
            right_location = right_side[numbers[i]]
            answer += 'R'
        else:
            middle_location = middle_side[numbers[i]]
            if abs(left_location[0] - middle_location[0]) + abs(left_location[1] - middle_location[1]) < abs(right_location[0] - middle_location[0]) + abs(right_location[1] - middle_location[1]):
                left_location = middle_side[numbers[i]]
                answer += 'L'
            elif abs(left_location[0] - middle_location[0]) + abs(left_location[1] - middle_location[1]) > abs(right_location[0] - middle_location[0]) + abs(right_location[1] - middle_location[1]):
                right_location = middle_side[numbers[i]]
                answer += 'R'
            else:
                if hand == 'left':
                    left_location = middle_side[numbers[i]]
                    answer += 'L'
                else:
                    right_location = middle_side[numbers[i]]
                    answer += 'R'
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
