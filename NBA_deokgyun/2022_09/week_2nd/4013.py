# 4013. 특이한 자석

import sys


def magnet_rotation(magnet_number, rotate_direction):
    global is_linked
    is_linked[magnet_number] = rotate_direction
    if magnet_number > 1 and is_linked[magnet_number - 1] == 0:
        if magnets[magnet_number - 1][2] != magnets[magnet_number][6]:
            magnet_rotation(magnet_number - 1, -rotate_direction)
    if magnet_number < 4 and is_linked[magnet_number + 1] == 0:
        if magnets[magnet_number + 1][6] != magnets[magnet_number][2]:
            magnet_rotation(magnet_number + 1, -rotate_direction)


sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    rotate_count = int(input())
    magnets = [0]
    for _ in range(4):
        magnets.append(list(map(int, input().split())))
    for _ in range(rotate_count):
        is_linked = [0] * 5
        magnet_num, rotate_dir = map(int, input().split())
        magnet_rotation(magnet_num, rotate_dir)
        for i in range(1, 5):
            if is_linked[i] == 1:
                magnets[i].insert(0, magnets[i].pop())
            if is_linked[i] == -1:
                magnets[i].append(magnets[i].pop(0))
    result_sum = 0
    for j in range(1, 5):
        result_sum += magnets[j][0] * (2 ** (j - 1))
    print(f"#{test_count}", result_sum)
