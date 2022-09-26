# [SWEA] 4008. 숫자 만들기


'''
아이디어

연산자 -> 순열 사용 (순서가 상관있음)


<문제>
1. 같은 연산자의 경우 순서가 상관 없음 -> 연산을 줄일 수 있음
    -> set 으로 중복 제거

2. 소수점 이하를 버리기 위해 // 연산자를 사용하면, 음수의 경우 몫이 -1 더 나옴
    -> 조건문으로 처리
    -> int로 가능 (정수형으로 바꾸기 위해 소수점을 버림)

3. 시간 초과...
    itertools.permutations 의 시간복잡도 == O(n!)

4. // 연산자 : 0으로 나누면 ZeroDivisionError
    -> 조건문으로 처리
'''

import time
import itertools

operator = ['+', '-', '*', '/']

cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

for tc in range(1, int(input()) + 1):

    n = int(input())

    use = ""
    operator_cnt = list(map(int, input().split()))
    for i in range(4):
        use += operator_cnt[i] * operator[i]

    numbers = list(map(int, input().split()))

    start_time = time.time()
    pmt = list(set(itertools.permutations(use, len(use))))
    print(pmt)

    print(time.time() - start_time)

    max_val = -100000000
    min_val = 100000000
    for i in range(len(pmt)):
        val = numbers[0]
        for j in range(n - 1):
            if pmt[i][j] == '/':
                if val < 0:
                    val = cal[pmt[i][j]](val, numbers[j + 1]) + 1
                elif numbers[j + 1] == 0:
                    pass
                else:
                    val = cal[pmt[i][j]](val, numbers[j + 1])
            else:
                val = cal[pmt[i][j]](val, numbers[j + 1])
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    print(f'#{tc} {max_val - min_val}')
