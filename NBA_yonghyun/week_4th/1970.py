# 쉬운 거스름돈

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    money_cnt = []

    # 큰 금액의 돈부터 고려
    for m in money:
        cnt = 0
        # 거슬러 줄 금액 n이 각 돈보다 크거나 같으면 계속해서,
        while n >= m:
            n = n - m  # 거스름돈에서 m의 값을 빼줌
            cnt += 1  # 사용한 돈의 개수는 계속해서 추가해줌
        money_cnt.append(cnt)

    # 프린트를 한번만 쓰는 방법은 없을까?
    print(f'#{test_case}')
    print(*money_cnt)
