# [Programmers] 42889. 실패율

from collections import defaultdict

def solution(N, stages):
    # stages 정보 합
    fail = defaultdict(int)
    for stage in stages:
        fail[stage] += 1
    
    # stages 정보로 실패율 계산
    fail_sorted = []
    temp = len(stages)
    for stage in range(1, N + 1):
        if temp == 0:
            fail_sorted.append((0, stage))
        else:
            cnt = fail[stage]
            fail_sorted.append((cnt/temp, stage))
            temp -= cnt

    # 정렬
    fail_sorted.sort(key=lambda x: (x[0], [1]), reverse=True)

    # 출력값 생성
    answer = []
    for fail_ratio, stage_num in fail_sorted:
        answer.append(stage_num)

    return answer


solution(4, [4,4,4,4,4])