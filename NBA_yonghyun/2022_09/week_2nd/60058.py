# 60058. 괄호 변환


def solution(p):
    global answer
    if not p:
        return p
    else:
        if p[0] == "(":
            return cor(p)
        else:
            return in_cor(p)


# u가 올바른 문자열일 때, 처리할 함수
def cor(st):
    u = ""  # 앞 문자열 (균형 잡힌)
    stack = []
    if st[0] == "(":
        for bracket in st:
            if bracket == "(":
                stack.append("(")
                u += "("
            else:
                stack.pop()
                u += ")"
                if not stack:
                    break
        # answer += u
        v = st[len(u) :]  # u, v 분리
        return u + solution(v)  # 3단계 (v에 대하여 1단계부터 처리)


# u가 올바른 문자열이 아닐 때, 처리할 함수 (4단계)
def in_cor(st):
    u2 = ""
    stack = []
    for bracket in st:
        if bracket == ")":
            stack.append(")")
            u2 += ")"
        else:
            stack.pop()
            u2 += "("
            if not stack:
                break
    v2 = st[len(u2) :]
    return "(" + solution(v2) + ")" + rev(u2)


# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
def rev(u):
    rev_u = ""
    for i in u[1:-1]:
        if i == "(":
            rev_u += ")"
        else:
            rev_u += "("
    return rev_u


answer = ""
u = ""


'''
느낀점

1. global 전역 변수 선언 남발하지 않기
-> 다른 함수에서도 영향을 미칠 수 있음

2. 프로그래머스는 return 값을 바로 반환함
-> 반환할 값을 제외하고는 식을 return 하는 등 값 리턴X
'''
