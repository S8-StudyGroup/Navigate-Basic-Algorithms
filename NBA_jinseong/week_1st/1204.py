# 최빈수 구하기
T = int(input())

for test_case in range(1, T + 1):
    test_num = int(input())
    scores = list(map(int, input().split()))
    num_count = dict()  # 키 : 숫자, 값 : 개수
    for score in scores:
        if num_count.get(score):  # dictionary에 해당 숫자에 대한 카운트가 있는 경우
            num_count[score] += 1
        else:  # 처음 세는 숫자면 key와 함께 값 1로 초기화
            num_count[score] = 1
    # 점수(key)의 개수(value)가 가장 높은 개수의 값(max())과 같으면 그 숫자(key)를 리스트에 저장
    maxnum_score = list()
    for k, v in num_count.items():
        if max(num_count.values()) == v:
            maxnum_score.append(k)

    print(f'#{test_num} ', end='')
    for num in maxnum_score:
        print(num, end=' ')
    print()
