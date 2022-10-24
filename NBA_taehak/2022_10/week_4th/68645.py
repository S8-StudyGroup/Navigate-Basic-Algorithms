# [Programmers] 68645. 삼각 달팽이

def solution(n):
    if n == 1:
        return [1]

    answer_0 = []
    for i in range(n + 1):
        answer_0.append([0] * i)
    r = 0
    c = 0

    d_r = [1, 0, -1]
    d_c = [0, 1, -1]
    di = 0
    num = 1
    while num <= n*(n+1)//2:
        next_r = r + d_r[di]
        next_c = c + d_c[di]

        if 0 <= next_r <= n and 0 <= next_c < next_r and answer_0[next_r][next_c] == 0:
            answer_0[next_r][next_c] = num
        else:
            di = (di + 1) % 3
            next_r = r + d_r[di]
            next_c = c + d_c[di]
            answer_0[next_r][next_c] = num
        
        r = next_r
        c = next_c
        num += 1

    answer = []
    for i in answer_0:
        answer.extend(i)
    return answer