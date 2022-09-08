# 60058. 괄호 변환

def is_correct(p):
    stack = []

    for i in p:
        if not stack:
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True


def is_balance(p):
    a = 0

    for i in p:
        if i == '(':
            a += 1
        else:
            a -= 1

    if a:
        return False
    else:
        return True


def reverse(p):
    result = ''
    for i in p:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result


def solution(p):
    if is_correct(p):
        return p

    for i in range(2, len(p) + 1, 2):
        if is_balance(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    if is_correct(u):
        u += solution(v)
        return u
    else:
        answer = ''
        answer += '(' + solution(v) + ')'
        u = reverse(u[1:-1])
        answer += u
        return answer