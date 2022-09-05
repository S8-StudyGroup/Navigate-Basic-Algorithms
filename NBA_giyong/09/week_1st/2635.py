# 2635. 수 이어가기
import sys

sys.stdin = open("input")

n = int(input())

max_list = []

for i in range(1, n + 1):
    result_list = [n, i]
    idx = 1
    while True:
        next_num = result_list[idx - 1] - result_list[idx]
        if next_num < 0:
            break
        result_list.append(next_num)
        idx += 1

    if len(max_list) < len(result_list):
        max_list = result_list

print(len(max_list))
for i in max_list:
    print(i, end=" ")

# print(*max_list)

