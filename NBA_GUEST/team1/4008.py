# [SWEA] 4008. 숫자 만들기
# Guest - 임성빈

from collections import deque
from copy import deepcopy

operator = ['+', '-', '*', '/']


def cal_result(numbers, operators, stack):

    # queue가 비어있을 경우 종료
    if not numbers:
        global min_value, max_value
        value = stack.pop()  # 수식으로 도출된 값
        if min_value > value:  # 현재 저장된 최솟값보다 도출된 값이 작을 경우
            min_value = value  # 최솟값에 도출된 값 할당
        if max_value < value:  # 현재 저장된 최댓값보다 도출된 값이 클 경우
            max_value = value  # 최댓값에 도출된 값 할당
        return  # 종료

    num_copy = deepcopy(numbers)  # list는 mutable 속성
    stack_num = stack.pop()  # 현재까지 계산된 값
    deque_num = num_copy.popleft()  # 남은 카드 리스트에서 첫번째 카드를 dequeue

    for i in range(4):  # 4 종류의 연사자 탐색
        if operators[i] != 0:  # 연산자 리스트에서 개수가 남아 있을 경우
            operators[i] -= 1  # 연산자 수를 1개 감소
            if i == 0:  # 연산자의 종류 구분
                result = stack_num + deque_num  # 현재까지 계산된 값과 첫번째 카드의 수를 연산
            elif i == 1:
                result = stack_num - deque_num
            elif i == 2:
                result = stack_num * deque_num
            elif i == 3:
                result = int(stack_num / deque_num)

            stack.append(result)  # 소수점을 제외 시키고 stack에 append

            cal_result(num_copy, operators, stack)  # 재귀

            operators[i] += 1  # 재귀의 끝까지 도달한 경우


# 최댓값
INF = 1000000000

for tc in range(1, int(input()) + 1):
    n = int(input())  # 카드의 개수
    operators = list(map(int, input().split()))  # 연산자의 종류별 수
    numbers = deque(map(int, input().split()))  # 카드 리스트
    stack = []  # 현재까지 계산된 값을 담을 stack

    min_value = INF  # 최솟값을 담을 변수
    max_value = INF * -1  # 최댓값을 담을 변수

    number = numbers.popleft()  # 첫번째 카드를 dequeue
    stack.append(number)  # stack에 첫번째 카드를 append

    cal_result(numbers, operators, stack)  # 카드 리스트, 연산자 리스트, stack를 인자로하는 cal_result 함수

    answer = max_value - min_value  # 최대값과 최소값의 차이

    print(f'#{tc} {answer}')
