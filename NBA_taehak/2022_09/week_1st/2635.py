# 2635. 수 이어가기

# 첫번째 풀이
# # 수 이어가기
# # 풀이시간: 35

# # 두번째 수는 (첫번째수/2) 부터 검색해보는 것이 괜찮을듯..

# # 첫번째 수 입력
# num = int(input())

# result_count = 0

# # num도 양수고 second_num도 항상 양수 만약 1 들어왔을때 num//2 만 하면 second_num에 0이 들어감 => 오류
# second_num = num // 2 + num % 2
# for num_2 in range(second_num, num + 1):
#     num_1 = num
#     this_count = 2
#     this_result = [num, num_2]
#     while 1:
#         num_3 = num_1 - num_2
#         if num_3 < 0:
#             break
#         else:
#             this_count += 1
#             this_result.append(num_3)
#         num_1, num_2 = num_2, num_3

#     if this_count > result_count:
#         result_count = this_count
#         result = this_result


# print(result_count)
# print(*result)


# 두번째 풀이
# 수 이어가기

n = int(input())
ans = [n, n + 1]
for i in range(n // 2, n + 1):
    result = [n, i]

    while result[-1] >= 0:
        result.append(result[-2] - result[-1])

    if len(result) > len(ans):
        ans = result

ans.pop()
print(len(ans))
print(*ans)
