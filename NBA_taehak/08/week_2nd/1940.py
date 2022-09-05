# 가랏! RC카!

'''
매 초 command 가 주어진다.
command 0: 속도 유지, 1: 가속, 2: 감속
command 1, 2 의 경우 가속도의 값이 추가로 주어진다.
N개의 command 를 모두 수행 했을 때 N초 동안 이동한 거리를 계산
초기속도 = 0
속도단위 m/s2
'''

'''
가속도가 아니라 0초만에 속도가 얼마나 변화했는지 입력값으로 주어지는 것
'''

import sys

sys.stdin = open('input_1940.txt')


for case in range(1, int(input()) + 1):
    n = int(input())

    d = 0
    t_v = {0: 0}

    for t in range(1, n + 1):
        command = input()

        if command[0] == '1':
            t_v[t] = t_v[t - 1] + int(command[-1])
        elif command[0] == '2':
            t_v[t] = t_v[t - 1] - int(command[-1])
            if t_v[t] < 0:
                t_v[t] = 0
        else:
            t_v[t] = t_v[t - 1]

        d += t_v[t]

    print(f'#{case} {d}')
