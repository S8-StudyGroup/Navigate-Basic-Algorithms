# 두 개의 숫자열

T = int(input())
for t in range(T):
    m, n = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    k = abs(m - n)

    multi_list = []
    multi = 0

    if m == n:
        for i in range(m):
            multi += a[i] * b[i]

        print(f'#{t + 1} {multi}')

    else:

        if m > n:

            for k in range(k + 1):

                for i in range(n):
                    multi += a[i + k] * b[i]

                multi_list.append(multi)
                multi = 0

        else:

            for k in range(k + 1):

                for i in range(m):
                    multi += a[i] * b[i + k]

                multi_list.append(multi)
                multi = 0

        multi_sort = sorted(multi_list, reverse=True)

        print(f'#{t + 1} {multi_sort[0]}')
