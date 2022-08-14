# 간단한 소인수분해

# 총 테스트 케이스 개수
T = int(input())

for test_case in range(1, T + 1):

    # 소수 리스트
    prime_numbers = [2, 3, 5, 7, 11]

    # a, b, c, d, e 저장할 변수
    pow = [0 for _ in range(len(prime_numbers))]

    # 입력받은 숫자 N
    N = int(input())

    for idx, prime_number in enumerate(prime_numbers):

        # 현재 소수로 더이상 인수분해되지 않을 때까지 반복
        while N % prime_number == 0:
            pow[idx] += 1
            N = N // prime_number

    # a, b, c, d, e 출력
    print(f'#{test_case} {" ".join(map(str, pow))}')
