# [Programmers] 92342. 양궁대회
from itertools import combinations_with_replacement
from copy import deepcopy


def solution(n, info):
    answer = []
    # 어피치가 맞춘 점수들
    score_0 = set()
    for score, cnt in enumerate(info[::-1]):
        if cnt > 0:
            score_0.add(score)

    # 경우의 수마다
    result = -1
    for scores in combinations_with_replacement(range(11), n):
        scores = list(scores)
        check = deepcopy(info[::-1])
        for score in scores:
            check[score] -= 1
        
        lion = 0
        apeach = 0
        for score, cnt in enumerate(check):
            if cnt < 0:
                lion += score
            # 어피치가 맞춘 점수, 어피치가 더 많이 맞춤
            elif score in score_0 and cnt >= 0:
                apeach += score

        # print(score_0, scores, check, lion, apeach)
        diff = lion - apeach

        if diff > result:
            result = diff
            answer = scores

    result = [0] * 11
    if sum(answer) == 0:
        result = [-1]
    for score in answer:
        result[score] += 1

    return result[::-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))