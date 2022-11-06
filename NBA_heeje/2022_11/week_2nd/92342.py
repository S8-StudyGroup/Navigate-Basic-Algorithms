# [Programmers] 92342. 양궁대회


def solution(n, info):
    def is_max_score_list(list1, list2):
        for i in range(len(list1) - 1, -1, -1):
            if list1[i] < list2[i]:
                return False
            if list1[i] > list2[i]:
                return True
        return False

    def dfs(idx, n, apeach_score, ryan_score, ryan_score_list):
        if n == 0 or idx == len(info):
            nonlocal max_difference, max_score_list
            difference = ryan_score - apeach_score
            if max_difference < difference or (
                0 < max_difference == difference
                and is_max_score_list(ryan_score_list, max_score_list)
            ):
                if n != 0:
                    ryan_score_list[-1] += n
                max_difference = difference
                max_score_list = ryan_score_list[:]
                if n != 0:
                    ryan_score_list[-1] -= n
            return

        new_ryan_score_list = ryan_score_list[:]
        if info[idx] == 0:
            new_ryan_score_list[idx] += 1
            dfs(
                idx + 1, n - 1, apeach_score, ryan_score + 10 - idx, new_ryan_score_list
            )
            new_ryan_score_list[idx] -= 1

        else:
            if info[idx] < n:
                new_ryan_score_list[idx] += info[idx] + 1
                dfs(
                    idx + 1,
                    n - (info[idx] + 1),
                    apeach_score - (10 - idx),
                    ryan_score + 10 - idx,
                    new_ryan_score_list,
                )
                new_ryan_score_list[idx] -= info[idx] + 1
        dfs(idx + 1, n, apeach_score, ryan_score, new_ryan_score_list)

    apeach_score = sum([idx if val else 0 for idx, val in enumerate(info[::-1])])
    max_difference = 0
    max_score_list = []
    dfs(0, n, apeach_score, 0, [0] * 11)

    if max_difference == 0:
        answer = [-1]
    else:
        answer = max_score_list
    return answer
