# 간단한 소인수분해

tc = int(input())

for i in range(tc):

    N = int(input())

    factors = [2, 3, 5, 7, 11]

    result = [0] * 5       ##결과를 넣을 변수

    for j in range(len(factors)):  ## factors를 돌면서 나눗셈을 한다. 만약 2로 나눈다면 나머지가 0인 동안은 계속 반복한다.
                                        ## 그리고 나머지가 0이면 인수를 더하기 1 해준다.
        while N % factors[j] == 0:
            N = N / factors[j]
            result[j] += 1

    print(f'#{i + 1}', end=' ')
    print(*result)
