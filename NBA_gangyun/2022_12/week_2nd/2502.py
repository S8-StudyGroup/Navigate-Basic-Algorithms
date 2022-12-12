# [BOJ] 2502. 떡 먹는 호랑이

day, rice = map(int, input().split())
dp = [(1, 0), (0, 1)]   # 문제에 주어진 a, b를 (a, b)의 형태로 표현하여 피보나치 배열의 첫 번째, 두 번째 값을 설정
                        # ex) 첫 날에 준 떡은 1 * a + 0 * b개 이므로 dp[0] = (1, 0)
                        # 두 번째 날에 준 떡은 0 * a + 1 * b개 이므로 dp[0] = (0, 1)

for i in range(2, 31):
    gain_a = dp[i - 1][0] + dp[i - 2][0]     # 전날과 전전날에 준 떡을 합치면 당일 a에 곱해질 수를 구할 수 있음
    gain_b = dp[i - 1][1] + dp[i - 2][1]     # 전날과 전전날에 준 떡을 합치면 당일 b에 곱해질 수를 구할 수 있음
    dp.append((gain_a, gain_b))

gain_a = dp[day - 1][0]     # 할머니가 넘어온 날의 a에 곱해질 수를 저장
gain_b = dp[day - 1][1]     # 할머니가 넘어온 날의 b에 곱해질 수를 저장

for a in range(1, rice):                # 첫 날 준 떡의 개수를 1부터 증가시켜가며 검사
    remain_rice = rice - gain_a * a     # 전체 떡의 개수에서 a 만큼을 뺀 값을 저장
    if remain_rice % gain_b == 0:       # 남은 떡의 개수가 b와 곱해질 수와 나누어 떨어지면
        b = remain_rice // gain_b       # 나누어 떨어진 그 값이 곧 b이다.
        if 1 <= a <= b:                 # 주어진 조건에 맞으면
            print(a)                    # a, b를 출력
            print(b)
            break
