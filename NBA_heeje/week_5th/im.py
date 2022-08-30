# 문제 요약
# 신입사원들을 점수 리스트와 두 개의 기준점수(T1, T2)를 이용하여 A, B, C반으로 나누려고 한다.
# 점수가 T2 이상일 땐 C반, T1 이상 T2 미만일 땐 B반, T1 미만일 땐 A반
# 이 때 각 반은 모두 최소 인원과 최대 인원을 만족하여야 하며, 조건에 맞게 반을 편성할 수 있는 방법이 없을 땐 -1을 반환한다.
# 반을 편성할 수 있는 방법이 여러가지라면 각 반에서 최대 인원과 최소 인원을 뺀 값이 최소인 값을 구하여라.

# 아이디어
# 1. 점수 리스트에서 최댓값을 구한 뒤 T1, T2를 최댓값 내의 범위에서 완전 탐색한다! (연산 약 10000번 예상)
# 2. 각 T1, T2가 정해질 때마다 점수 리스트를 탐색하며 알맞은 반에 넣어준다! (연산 약 1000번 예상 - N이 1000 이하인 수이기 때문)
# 3. 꾸려진 반이 조건에 맞다면 각 반에서 최대 인원과 최소 인원을 뺀 값을 구하여 최솟값과 비교한다.
# 연산 약 1천만번(10000 * 1000) 예상, 주어진 시간 넉넉함! 실행가능!
T = int(input())

for tc in range(1, T + 1):
    N, K_min, K_max = map(
        int, input().split()
    )  # N : 사원의 수, K_min : 최소 인원, K_max : 최대 인원
    scores = list(map(int, input().split()))  # scores : 사원들의 점수
    max_score = max(scores)
    answer = -1  # 조건에 맞게 반을 편성할 수 없는 경우 초기값인 -1 반환

    for T1 in range(1, max_score):  # T1, T2 : 반을 나누는 기준 점수
        for T2 in range(T1 + 1, max_score + 1):  # 최대 점수 내에서 T1, T2가 될 수 있는 모든 경우의 수를 탐색
            classroom = {'A': 0, 'B': 0, 'C': 0}  # 반 배정 딕셔너리

            # T1, T2에 따라 반을 배정한다.
            for score in scores:  # 점수 리스트 탐색
                if score < T1:  # 점수가 T1 미만일 경우 A반 편성
                    classroom['A'] += 1
                elif T1 <= score < T2:  # 점수가 T1 이상, T2 미만일 경우 B반 편성
                    classroom['B'] += 1
                else:  # 점수가 T2 이상일 경우 C반 편성
                    classroom['C'] += 1

            # 반 인원이 최소 인원보다 적거나 최대 인원보다 많다면 넘어간다.
            for room in ['A', 'B', 'C']:
                if classroom[room] < K_min or classroom[room] > K_max:
                    break

            # 반 인원이 알맞게 편성된 경우
            # 가장 많은 인원으로 구성된 분반과 가장 적은 인원으로 구성된 분반의 인원 수 차이 값을 구한 뒤
            # 현재 저장되어있는 최솟값과 비교한다.
            else:
                minimum = max(classroom.values()) - min(classroom.values())
                if answer == -1:
                    answer = minimum
                else:
                    if answer > minimum:
                        answer = minimum
                # minimum = max(classroom.values()) - min(classroom.values())
                # if answer == -1:
                #     answer = max(classroom.values()) - min(classroom.values())
                # else:
                #     if answer > max(classroom.values()) - min(classroom.values()):
                #         answer = max(classroom.values()) - min(classroom.values())

    print(f"#{tc} {answer}")
