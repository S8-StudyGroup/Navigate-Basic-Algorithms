# [Programmers] 67256. 키패드 누르기

def solution(numbers, hand):
    left = 9
    right = 11
    answer = ''
    for i in numbers:
        i = i - 1
        if i == -1:
            i = 10
        if i % 3 == 1:
            l2 = abs(left // 3 - i // 3) + abs(left % 3 - i % 3)
            r2 = abs(right // 3 - i // 3) + abs(right % 3 - i % 3)
            if l2 == r2:
                if hand == "left":
                    left = i
                    answer += "L"
                else:
                    right = i
                    answer += "R"
            elif l2 > r2:
                right = i
                answer += "R"
            else:
                left = i
                answer += "L"
        elif i % 3 == 0:
            left = i
            answer += "L"
        else:
            right = i
            answer += "R"
    return answer