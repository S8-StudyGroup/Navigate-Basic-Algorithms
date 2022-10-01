# 1220. Magnetic

import sys

sys.stdin = open('1220input.txt')

for test_case in range(1, 11):
    num = int(input())
    table = [list(map(int, input().split())) for _ in range(num)]
    count = 0

    for i in range(num):
        row_count = 0
        crash_counter = []
        for j in range(num):
            if table[j][i] == 1:
                crash_counter.append(1)
            elif table[j][i] == 2:
                crash_counter.append(2)

        for i in range(len(crash_counter) - 1):
            if crash_counter[i] == 1 and crash_counter[i + 1] == 2:
                count += 1

    print(f'#{test_case} {count}')
    