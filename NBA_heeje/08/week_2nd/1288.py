# 새로운 불면증 치료법

T = int(input())

for test_case in range(1, T + 1):

    # 본 숫자를 보관할 리스트
    numbers = []

    # N 입력 받아 저장
    N = int(input())

    # N에 곱할 수와 양을 센 횟수 저장
    k = 0

    # numbers에 0 ~ 9가 다 있을 때까지 반복
    while len(numbers) < 10:

        # k에 N을 곱한 값을 문자열로 저장
        k += 1
        kN = str(k * N)

        # numbers 안에 없는 숫자가 있을 시 numbers에 추가
        for i in range(len(kN)):
            if kN[i] not in numbers:
                numbers.append(kN[i])

    # k값 출력
    print(f"#{test_case} {k * N}")
