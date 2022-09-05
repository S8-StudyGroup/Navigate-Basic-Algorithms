# 최빈수 구하기

T = int(input())

for test_case in range(T):
    test_num = int(input())

    scores = list(map(int, input().split()))

    re_score_list = []

    # 받은 scores 리스트 내 숫자의 개수 세기
    for i in range(len(scores)):
        re_score = 0

        for j in range(len(scores)):
            if scores[i] == scores[j]:
                re_score += 1

        re_score_list.append(re_score)  # 리스트로 할당

    # 가장 많이 나온 숫자의 횟수와 그 인덱스를 찾음
    max_score_num = re_score_list[0]
    max_score_index = 0

    for i in range(1, len(re_score_list)):
        # 최빈값이 1개일 때
        if re_score_list[i] > max_score_num:
            max_score_num = re_score_list[i]
            max_score_index = i

        # 최빈값이 2개 이상이어서 대소비교를 해야할 때
        elif re_score_list[i] == max_score_num:
            if scores[i] > scores[max_score_index]:
                max_score_num = re_score_list[i]
                max_score_index = i

    print(f'#{test_num} {scores[max_score_index]}')
