# 새로운 불면증 치료법

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     sheep_counter = [0] * 10

#     for num in range(N, 10**6 + 1, N):
#         for sheep in str(num):
#             sheep_counter[int(sheep)] += 1
#             num_count = 0
#             for i in range(10):
#                 if sheep_counter[i] > 0:
#                     num_count += 1
#         if num_count == 10:
#             result = num

#     print(f'#{test_case} {result}')
#
# ----------테스트 케이스 100개중 34개----------

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    sheep_counter = [0] * 10
    sheep = N

    while True:
        num_count = 0
        for num in str(sheep):
            sheep_counter[int(num)] += 1

        for i in range(10):
            if sheep_counter[i] > 0:
                num_count += 1

        if num_count == 10:
            result = N
            break

        sheep += N

    print(f'#{test_case} {sheep}')
