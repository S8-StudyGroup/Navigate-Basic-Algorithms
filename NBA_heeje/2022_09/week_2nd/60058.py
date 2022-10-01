def solution(p):
    if is_right(p):  # 입력이 빈 문자열이거나
        return p  # 이미 올바른 괄호 문자열일 경우 그대로 반환

    bracket_cnt = {"(": 0, ")": 0}  # 괄호 카운트

    for i in range(len(p)):  # u와 v를 분리해주기 위해 u의 범위를 찾는다.
        bracket_cnt[p[i]] += 1
        if bracket_cnt["("] == bracket_cnt[")"]:  # "("와 ")"의 개수가 같다면 u로 분리
            u = p[: i + 1]
            v = p[i + 1 :]
            break

    if is_right(u):  # u가 올바른 괄호 문자열이라면 문자열 v에 대해
        return u + solution(v)  # 1단계부터 수행 후 그 값을 u 뒤에 붙여 반환
    else:
        new_u = ""  # u가 올바른 괄호 문자열이 아니라면
        for i in range(1, len(u) - 1):  # u의 첫 번째와 마지막 문자롤 제거하고
            new_u += "(" if u[i] == ")" else ")"  # 나머지 문자열의 괄호 방향을 뒤집는다.

        return "(" + solution(v) + ")" + new_u  # 괄호 사이에 문자열 v에 대해 재귀수행한 결과를
        # 넣고 뒤에 새롭게 만들어진 u를 붙여 반환


def is_right(brackets):  # 올바른 괄호 문자열 판별 함수
    stack = []  # 스택 활용
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    return False if stack else True  # 작업이 끝난 후 스택이 남아있다면 False
