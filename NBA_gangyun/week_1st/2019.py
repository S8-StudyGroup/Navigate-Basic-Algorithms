# 더블더블

# num = int(input())
# num_double = 1

# for i in range(num + 1):
#     if i == 0:
#         num_double = 1    # 2의 0제곱 == 1
#     else :
#         num_double *= 2   # i가 반복한 횟수만큼 2가 곱해짐
#     print(num_double, end=' ')

a = int(input())
list_b = [int(2**i) for i in range(a + 1)]  # list comprehension 이용
print(*list_b)  # Asterisk(*)를 이용하여 리스트를 unpakcing
