# [Programmers] 92342. 양궁대회
from itertools import combinations_with_replacement
from copy import deepcopy


def solution(n, info):
    answer = []

    info = info[::-1]
    # 어피치가 맞춘 점수들
    score_0 = set()
    for score, cnt in enumerate(info):
        if cnt > 0:
            score_0.add(score)

    # 경우의 수마다
    score_diff_max = 1
    for scores in combinations_with_replacement(range(11), n):
        check = deepcopy(info)
        for score in scores:
            check[score] -= 1
        
        lion = 0
        apeach = 0
        for score, cnt in enumerate(check):
            if cnt < 0:
                lion += score
            # 어피치가 맞춘 점수, 어피치가 더 많이 맞춤
            elif cnt >= 0 and score in score_0 :
                apeach += score

        # print(score_0, scores, check, lion, apeach)
        score_diff = lion - apeach

        if score_diff > score_diff_max:
            score_diff_max = score_diff
            answer = [tuple(scores)]
        elif score_diff == score_diff_max and score_diff_max != -1:
            answer.append(tuple(scores))
    

    final_result = []
    for score_case in answer:
        result = [0] * 11
        for i in score_case:
            result[i] += 1
        final_result.append(deepcopy(result[::-1]))
            
    if len(final_result) > 1:
        for i in range(11):
            final_result = sorted(final_result, key = lambda x : x[i])

    rr = []
    if not final_result:
        rr = [-1]
    elif sum(final_result[-1]) == 0:
        rr = [-1]
    else:
        rr = final_result[-1]

    return rr


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))