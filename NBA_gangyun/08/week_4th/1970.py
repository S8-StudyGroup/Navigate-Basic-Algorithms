# 쉬운 거스름돈

# 그리디 알고리즘을 활용
for test_case in range(1, int(input()) + 1):
    N = int(input())
    money_type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   # 화폐의 종류
    money_counter = [0] * 8     # 화폐를 종류별로 카운트할 배열을 생성

    # 가장 액수가 큰 화폐를 먼저 사용이 가능한지 확인
    for i in range(8):
        if N >= money_type[i]:  # 액수가 해당 화폐의 단위보다 크다면
            money_counter[i] += N // money_type[i]  # 단위로 나눠지는 만큼 화폐의 개수를 카운트
            N = N % money_type[i]   # 화폐 단위로 나눈 나머지를 다시 N으로 설정하여 다음 반복문에 사용

    print(f'#{test_case}')
    print(*money_counter)



