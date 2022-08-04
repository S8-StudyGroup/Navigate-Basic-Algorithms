# 두 개의 숫자열

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A_i = list(map(int, input().split()))
    B_j = list(map(int, input().split()))

    if len(A_i) > len(B_j):
        A_i, B_j = B_j, A_i
        N, M = M, N

    sum_list = []

    for move in range(M - N + 1):
        product_AB = [A_i[iter] * B_j[iter + move] for iter in range(N)]
        sum_product_AB = sum(product_AB)
        sum_list.append(sum_product_AB)

    print(f'#{test_case} {max(sum_list)}')

# 2022. 07. 10. 풀이
# T = int(input())

# for test_case in range(1, T + 1):
#     A_length, B_length = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     list_product_AB = []
#     sumproduct_AB = []

#     for i in range(0, abs(B_length - A_length)+1):
#         if A_length <= B_length:
#             for j in range(0, len(A)):
#                 list_product_AB.append(A[j] * B[j+i])
#             sumproduct_AB.append(sum(list_product_AB))
#             del list_product_AB[0: len(A)+1]
#         else:
#             for j in range(0, len(B)):
#                 list_product_AB.append(B[j] * A[j+i])
#             sumproduct_AB.append(sum(list_product_AB))
#             del list_product_AB[0: len(B)+1]

#     print('#' + str(test_case), max(sumproduct_AB))
