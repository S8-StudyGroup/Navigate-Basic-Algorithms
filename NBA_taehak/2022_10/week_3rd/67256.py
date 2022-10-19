# [Programmers] 67256. 키패드 누르기
def solution(numbers, hand):
    answer = ''
    
    left = {
        1: 0,
        4: 1,
        7: 2,
    }

    right = {
        3: 0,
        6: 1,
        9: 2,
    }

    middle = {
        2: 0,
        5: 1,
        8: 2,
        0: 3,
    }

    left_idx = [3, 0]
    right_idx = [3, 0]
    for num in numbers:
        if num in left:
            answer += 'L'
            left_idx = [left[num], 0]
        elif num in right:
            answer += 'R'
            right_idx = [right[num], 0]
        else:
            next_idx = middle[num]

            l_diff = abs(left_idx[0] - next_idx)
            r_diff = abs(right_idx[0] - next_idx)
            if not left_idx[1]:
                l_diff += 1
            if not right_idx[1]:
                r_diff += 1

            if l_diff < r_diff:
                answer += 'L'
                left_idx = [next_idx, 1]
            elif l_diff > r_diff:
                answer += 'R'
                right_idx = [next_idx, 1]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_idx = [next_idx, 1]
                else:
                    answer += 'R'
                    right_idx = [next_idx, 1]
            

    return answer