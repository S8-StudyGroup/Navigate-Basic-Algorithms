# [SWEA] 4008. 숫자 만들기
## 문제풀이 아이디어: 연산자의 개수가 6개이고, +, +, -, -, *, / 가 나타난다고 하자.
## 그렇다면 6개를 줄세우는 방법은 [ , , , , , ] 6개의 자리중에서 +자리 2개 정하고, -자리 2개 정하고, *자리 1개 정하고, /자리 1개 정하는것.

from itertools import combinations
import copy

tc = int(input())

for i in range(tc):
    N = int(input())
    each_oper_occur = list(map(int, input().split()))                                   ##각 연산자의 등장 횟수
    numbers = list(map(int, input().split()))
    length = N - 1                                                                      ##연산자 개수
    max_0 = -100000000
    min_0 = 100000000
    index_list = [k for k in range(length)]                                              
    index_set = set(index_list)                                                         ##N-1개의 자리 인덱스들. ex) 0,1,2,...,N-2
    oper_tmp = [0] * length                                                         
    for first in combinations(index_set, each_oper_occur[0]):
        for first_0 in first:
            oper_tmp[first_0] = '+'
        for second in combinations(index_set - set(first), each_oper_occur[1]):
            for second_0 in second:
                oper_tmp[second_0] = '-'
            for third in combinations(index_set - set(first) - set(second), each_oper_occur[2]):
                for third_0 in third:
                    oper_tmp[third_0] = '*'
                for fourth in combinations(index_set - set(first) - set(second) - set(third), each_oper_occur[3]):
                    for fourth_0 in fourth:
                            oper_tmp[fourth_0] = '/'    
                    tmp = copy.deepcopy(numbers)                                       ##numbers 그대로 가져오기
                    for j in oper_tmp:
                            if j == '+':                                               ##앞 2개 숫자 뽑아서 계산한다음 
                                left = tmp.pop(0)                                      ##다시 맨 앞에 넣어주기.
                                right = tmp.pop(0)
                                tmp.insert(0, left + right)
                            elif j == '-':
                                left = tmp.pop(0)
                                right = tmp.pop(0)
                                tmp.insert(0, left - right)
                            elif j == '*':
                                left = tmp.pop(0)
                                right = tmp.pop(0)
                                tmp.insert(0, left * right)
                            else:
                                left = tmp.pop(0)
                                right = tmp.pop(0)
                                tmp.insert(0, int(left / right))
                    if tmp[0] >= max_0:                                                ##최대 최소 구하기.
                        max_0 = tmp[0]
                    if tmp[0] <= min_0:
                        min_0 = tmp[0]
    
    result = max_0 - min_0
    print(f'#{i + 1} {result}')