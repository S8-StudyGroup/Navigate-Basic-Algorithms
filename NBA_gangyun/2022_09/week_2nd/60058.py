# 60058. 괄호 변환


# "올바른 괄호 문자열"일 경우 1, 아닐 경우 0을 반환해주는 함수
def bracket_checker(my_string):
    stack = []
    bracket_check = 1

    # "("을 만날 시 stack에 "("를 push, ")"을 만날 시 stack에서 pop
    for bracket in my_string:
        if bracket == "(":
            stack.append(bracket)
        else:

            # 스택이 비어있는데 pop을 시도하려고 하면 0을 반환하고 반복을 종료
            if not stack:
                bracket_check = 0
                break
            # 스택이 비어있지 않으면 pop
            else:
                stack.pop()

    return bracket_check


# 입력된 문자열을 명세를 따라 u, v로 분리해주는 함수
def slicing(my_string):
    u, v = "", ""
    open_check, close_check = 0, 0

    # 여는 괄호와 닫는 괄호의 개수가 같아지는 시점에서 u와 v로 분리
    for i in range(len(my_string)):
        if my_string[i] == "(":
            open_check += 1
            u += my_string[i]
        elif my_string[i] == ")":
            close_check += 1
            u += my_string[i]

        if open_check == close_check:
            v = my_string[len(u)::]
            break

    return u, v


def solution(p):
    answer = ""

    # 1
    if bracket_checker(p) == 1:
        return p

    else:
        # 2번 과정
        u, v = slicing(p)           

        # 3번 과정
        if bracket_checker(u):
            return u + solution(v)  # 3-1
        else:
            # 4-1 ~ 4-3 과정
            answer = "(" + solution(v) + ")"

            # 4-4 과정
            new_bracket = u[1: len(u) - 1:]
            for bracket in new_bracket:
                if bracket == "(":
                    answer += ")"
                else:
                    answer += "("
        return answer


print(solution(")("))
