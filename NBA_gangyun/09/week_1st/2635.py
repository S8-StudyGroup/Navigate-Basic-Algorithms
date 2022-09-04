# 2635. 수 이어가기

num = int(input())
max_length = []

# range(1, num)에서 반복을 돌릴경우 num = 1일 때 테스트 케이스가 틀림
for a_2 in range(1, num + 1):
    a_1 = num
    nums = [a_1, a_2]
    while a_1 - a_2 >= 0:
        a_3 = a_1 - a_2
        a_1, a_2 = a_2, a_3
        nums.append(a_3)
    if len(nums) > len(max_length):
        max_length = nums

print(len(max_length))
print(*max_length)

