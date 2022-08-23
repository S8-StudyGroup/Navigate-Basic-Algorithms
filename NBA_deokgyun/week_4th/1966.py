# 숫자를 정렬하자
import sys

sys.stdin = open("input.txt")
for test_count in range(1, int(input()) + 1):
    n = input()
    print(f"#{test_count}", *sorted(list(map(int, input().split()))))


# sorted 안쓰는 풀이

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))

    sorted_list = []

    while N_list:
        min_value = N_list[0]
        pop_index = 0
        for i, j in enumerate(N_list):
            if min_value > j:
                min_value = j
                pop_index = i
        sorted_list += [N_list.pop(pop_index)]

    print(f"#{test_count}", *sorted_list)
