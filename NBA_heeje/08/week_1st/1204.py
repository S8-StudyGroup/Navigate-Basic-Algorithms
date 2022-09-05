# 최빈수 구하기

# 테스트 케이스 입력 받아 저장
T = int(input())

# 각 테스트 케이스
for _ in range(1, T + 1):

    # 테스트 케이스의 번호 저장
    test_case = int(input())

    # 수학 성적 리스트에 내림차순으로 정렬하여 저장 (내림차순의 이유 : 최빈수가 여러 개일 때에는 가장 큰 정수를 출력해야 하기 때문)
    math_score = sorted(list(map(int, input().split())), reverse=True)

    # [최빈수, 개수] 초기 저장
    mode_info = [math_score[0], 1]

    # 반복문 돌 때 개수 세는 변수 저장
    n = 1

    for i, v in enumerate(math_score):
        # 이전 값과 점수가 다를 경우 현재 최빈수 개수와 비교하여 더 클 경우 최빈수 교체
        if v != math_score[i - 1]:
            if n > mode_info[1]:
                mode_info[0] = math_score[i - 1]
                mode_info[1] = n
            n = 1
        # 이전 값과 점수가 같을 경우 개수 + 1
        else:
            n += 1
    # 마지막 값 검사하기
    else:
        if n > mode_info[1]:
            mode_info[0] = math_score[999]
            mode_info[1] = n

    # 최빈수 값 출력
    print(f"#{test_case} {mode_info[0]}")
