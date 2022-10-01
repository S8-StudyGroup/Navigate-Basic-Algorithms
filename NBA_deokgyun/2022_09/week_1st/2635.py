# 2635. 수 이어가기

the_number = int(input())

max_length = 0
max_list = []
# the_number + 1 이라고 하지 않으면 틀리는데 아무래도 1이 주어질때가 있는 것 같다
for n in range(the_number // 2 + 1, the_number + 1):
    numbers_list = [the_number]
    numbers_list.append(n)
    while numbers_list[-1] >= 0:
        numbers_list.append(numbers_list[-2] - numbers_list[-1])
    numbers_list.pop()
    if len(numbers_list) >= max_length:
        max_length = len(numbers_list)
        max_list = numbers_list
print(max_length)
print(*max_list)
