# 두 개의 숫자열
T = int(input())

for test_case in range(1, T + 1):
    nm = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    n, m = nm[0:2]
    results = list()

    if n >= m:
        for i in range(n - m + 1):
            multi = 0
            for j, v in enumerate(bj):
                multi += ai[i + j] * bj[j]
            results.append(multi)
    else:  # m > n
        for i in range(m - n + 1):
            multi = 0
            for j, v in enumerate(ai):
                multi += bj[i + j] * ai[j]
            results.append(multi)

    print(f'#{test_case} {max(results)}')
