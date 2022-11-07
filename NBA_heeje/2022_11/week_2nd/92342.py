# [Programmers] 92342. 양궁대회


def solution(n, info):

    def is_max_score_list(list1, list2):                # 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이
        for i in range(len(list1) - 1, -1, -1):         # 여러 가지일 경우, 가장 낮은 점수를 더 많이
            if list1[i] < list2[i]:                     # 맞힌 경우를 찾는 함수
                return False                            # 두 리스트를 거꾸로(낮은 점수부터) 탐색하여
            if list1[i] > list2[i]:                     # ryan_score_list가 max_score_list보다
                return True                             # 가장 낮은 점수를 더 많이 맞혔을 때만 True를 반환
        return False

    # idx: info를 탐색할 인덱스
    # n: 남은 화살의 개수
    # apeach_score: 현재 어피치 점수
    # ryan_score: 현재 라이언 점수
    # ryan_score_list: 라이언이 맞힌 점수의 개수 리스트
    def dfs(idx, n, apeach_score, ryan_score, ryan_score_list):

        if n == 0 or idx == len(info):                  # 종료조건 : 화살을 모두 쐈거나 idx로 info를 모두 순환하였을 경우
            nonlocal max_difference, max_score_list
            difference = ryan_score - apeach_score      # 라이언의 점수와 어피치의 점수의 차이값을 저장
            if max_difference < difference or (         # 저장된 최대 차이보다 현재 차이가 더 클 때, 그리고
                0 < max_difference == difference        # 차이가 같으면서 가장 낮은 점수를 더 많이 맞혔다면 저장된 값과 교체 가능
                and is_max_score_list(ryan_score_list, max_score_list)
            ):
                if n != 0:                              # 쏴야 할 화살이 남아있다면
                    ryan_score_list[-1] += n            # 0점에 다 넣어준다(가장 낮은 점수를 더 많이 맞힌게 우선순위라서)

                max_difference = difference             # 저장된 최대 차이값과 현재 차이값을 교체
                max_score_list = ryan_score_list[:]     # 저장된 점수 리스트와 현재 점수 리스트를 교체(얕은 복사)

                if n != 0:                              # 0점에 다 넣어준 화살 되돌리기
                    ryan_score_list[-1] -= n            # 어차피 바로 return 되기 때문에 필요없을 것 같다.
            return

        new_ryan_score_list = ryan_score_list[:]        # 라이언의 점수 리스트 복사(다른 재귀에 영향을 끼치지 않기 위함)

        if info[idx] == 0:                              # 어피치가 해당 점수 과녁에 한 발도 맞히지 못했다면
            new_ryan_score_list[idx] += 1               # 라이언은 한 발만으로 해당 과녁의 점수를 얻을 수 있음
            dfs(                                        # 다음 dfs 진행
                idx + 1, n - 1, apeach_score, ryan_score + 10 - idx, new_ryan_score_list
            )
            new_ryan_score_list[idx] -= 1               # 작업 복구

        else:                                       # 어피치가 해당 점수 과녁에서 점수를 얻은 경우
            if info[idx] < n:                       # 현재 남아있는 화살의 개수가 현재 과녁에 어피치가 맞춘 화살 개수보다 크다면
                new_ryan_score_list[idx] += info[idx] + 1   # 어피치가 맞춘 화살 개수 + 1만큼 많이 맞혀본다.
                dfs(                                        # 이 경우, 재귀할 때 어피치의 점수도 해당 과녁의 점수만큼 빼준다.
                    idx + 1,
                    n - (info[idx] + 1),
                    apeach_score - (10 - idx),
                    ryan_score + 10 - idx,
                    new_ryan_score_list,
                )
                new_ryan_score_list[idx] -= info[idx] + 1   # 작업 복구

        dfs(idx + 1, n, apeach_score, ryan_score, new_ryan_score_list)  # 라이언이 해당 과녁을 맞히지 않고 넘어가는 경우

    apeach_score = sum([idx if val else 0 for idx, val in enumerate(info[::-1])])
    max_difference = 0                      # 라이언과 어피치 점수의 최대 차이
    max_score_list = []                     # 최대 차이일 때 라이언의 점수 리스트
    dfs(0, n, apeach_score, 0, [0] * 11)    # dfs 실행

    if max_difference == 0:                 # 모든 경우에서 라이언의 점수가 어피치의 점수보다 낮거나 같으면
        answer = [-1]                       # [-1] 반환
    else:                                   # 그렇지 않다면
        answer = max_score_list             # max_score_list 반환
    return answer
