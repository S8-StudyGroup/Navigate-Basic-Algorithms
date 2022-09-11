# 4013. 특이한 자석

import sys
from collections import deque
sys.stdin = open('4013input.txt')


def magnet_rotate(magnet_number, direction):
    if direction == 1:
        magnets[magnet_number].appendleft(magnets[magnet_number].pop())

    elif direction == -1:
        magnets[magnet_number].append(magnets[magnet_number].popleft())


for test_case in range(1, int(input()) + 1):
    K = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    rotate_info = [list(map(int, input().split())) for _ in range(K)]
    score = 0

    for magnet_num, direction in rotate_info:
        dir_list = [0, 0, 0, 0]
        dir_list[magnet_num - 1] = direction
        for i in range(magnet_num, 4):
            if magnets[i][6] != magnets[i - 1][2]:
                if (magnet_num - 1) % 2 == i % 2:
                    dir_list[i] = direction
                else:
                    dir_list[i] = -direction
            else:
                break

        for i in range(magnet_num - 1, -1, -1):
            if i < magnet_num - 1:
                if magnets[i][2] != magnets[i + 1][6]:
                    if (magnet_num - 1) % 2 == i % 2:
                        dir_list[i] = direction
                    else:
                        dir_list[i] = -direction
                else:
                    break

        for num in range(4):
            magnet_rotate(num, dir_list[num])

    for i in range(4):
        score += 2 ** i * magnets[i][0]

    print(f'#{test_case} {score}')