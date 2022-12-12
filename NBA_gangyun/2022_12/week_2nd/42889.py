# [Programmers] 42889. 실패율

def solution(N, stages):
    stage_failed = [0] * (N + 2)
    stage_challengers = [0] * (N + 2)
    for stage in stages:
        for i in range(1, stage + 1):
            stage_challengers[i] += 1
            if i == stage:
                stage_failed[i] += 1

    fail_info = []
    for i in range(1, N + 1):
        if stage_challengers[i] == 0:
            fail_info.append((i, 0))
        else:
            fail_info.append((i, stage_failed[i] / stage_challengers[i]))

    fail_info.sort(key=lambda x: x[1], reverse=True)
    answer = [fail_info[i][0] for i in range(N)]
    return answer