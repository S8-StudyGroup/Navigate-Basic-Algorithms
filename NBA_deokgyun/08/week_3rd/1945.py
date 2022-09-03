# 간단한 소인수분해

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    uppers_list = []
    for i in [2, 3, 5, 7, 11]:
        number_uppper = 0
        while N % i == 0:
            N = N / i
            number_uppper += 1
        uppers_list += [number_uppper]
    print(f"#{test_count}", *uppers_list)
