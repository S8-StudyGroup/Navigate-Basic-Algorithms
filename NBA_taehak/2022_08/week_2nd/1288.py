# 새로운 불면증 치료법

import sys

sys.stdin = open('input_1288.txt')

for case in range(1, int(input()) + 1):
    n = int(input())

    sheep = 0
    zero_ten = '1234567890'

    while zero_ten != '':
        sheep += 1
        n_sheep = n * sheep
        for i in str(n_sheep):
            zero_ten = zero_ten.replace(i, '')

    print(f'#{case} {n_sheep}')
