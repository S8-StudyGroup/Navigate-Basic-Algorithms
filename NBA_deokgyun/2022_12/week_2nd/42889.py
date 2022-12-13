# [Programmers] 42889. 실패율


def solution(N, stages):
    numlist = [0] * (N + 2)
    sumlist = [0] * (N + 2)
    numsum = 0
    for i in stages:
        numlist[i] += 1
        sumlist[i] += 1
    for i in range(N + 1, 0, -1):
        sumlist[i] = sumlist[i] + numsum
        numsum = sumlist[i]
    failslist = []
    answer = []
    for i in range(1, N + 1):
        if sumlist[i] != 0:
            failslist.append((i, numlist[i] / sumlist[i]))
        else:
            failslist.append((i, 0))
    for i in sorted(failslist, key=lambda x: (-x[1], x[0])):
        answer.append(i[0])
    return answer
