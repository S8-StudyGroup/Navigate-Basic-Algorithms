# [Programmers] 42889. 실패율


def solution(N, stages):
    failed_ratio_list = [[i, 0] for i in range(0, N + 1)]  # 실패율 저장 리스트
    sorted_stages = sorted(stages) + [0]  # 사용자가 멈춰있는 스테이지 번호 정렬 + 마지막에 0 추가
    prev = sorted_stages[0]  # 정렬된 리스트의 0번째 값 저장
    failed_ratio = [0, len(stages)]  # 실패율 초기 설정(해당 스테이지 실패 수 / 총 사용자 수)
    for stage in sorted_stages:
        if stage < N + 1 and prev == stage:  # 해당 스테이지가 마지막 스테이지가 아니고 이전과 같다면
            failed_ratio[0] += 1  # 실패율 조정

        else:  # 아니라면
            failed_ratio_list[prev][1] = (
                failed_ratio[0] / failed_ratio[1]
            )  # failed_ratio_list에 실패율 저장
            failed_ratio[0], failed_ratio[1] = (
                1,
                failed_ratio[1] - failed_ratio[0],
            )  # failed_ratio 초기화
            prev = stage  # 이전 값 갱신

            if stage == N + 1:  # 마지막 스테이지라면 탈출
                break
    failed_ratio_list = sorted(
        failed_ratio_list[1:], key=lambda x: x[1], reverse=True
    )  # 실패율 저장 리스트를 실패율로 정렬
    answer = list(map(lambda x: x[0], failed_ratio_list))  # 인덱스 값만 추출

    return answer
