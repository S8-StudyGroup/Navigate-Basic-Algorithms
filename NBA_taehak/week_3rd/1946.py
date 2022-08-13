# 간단한 압축풀기

import sys

sys.stdin = open('input_1946.txt')

for case in range(1, int(input()) + 1):
    temp = ''
    for j in range(int(input())):
        abc, num = input().split()
        temp += abc * int(num)

    print(f'#{case}')

    while len(temp) > 0:
        print(temp[:10])
        temp = temp[10:]
