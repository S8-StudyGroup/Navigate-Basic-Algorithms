import math
from collections import deque


def solution(numbers):

    # 중위순회
    def inorder(n):
        if n < len(bin_tree):
            inorder(2*n)
            bin_tree[n] = bin_num.popleft()
            inorder(2*n + 1)


    # 누군가의 부모 노드가 0이면 False
    def check():
        for i in range(2, len(bin_tree)):
            if bin_tree[i] == '1' and bin_tree[i//2] == '0':        # 이진트리 값이 1인 노드의 부모 노드가 0이면 False
                return False
        else:
            return True


    # 진행
    answer = []
    for number in numbers:
        bin_num = bin(number)[2:]                           # 주어진 숫자를 이진수로 변환
        height = int(math.log2(len(bin_num))) + 1           # 만들어야 하는 이진트리의 높이
        bin_tree = [0] * (2 ** (height))                    # 이진트리 생성 및 초기화

        bin_num = '0' * (len(bin_tree) - len(bin_num) - 1) + bin_num    # 포화 이진트리 생성하기 위해 앞에 0 더하기
        # print(bin_num)
        bin_num = deque(bin_num)

        inorder(1)                                          # 중위순회 하면서 이진수를 이진트리에 넣기
        # print(bin_tree)

        if check():
            answer.append(1)                                        
        else:
            answer.append(0)


    return answer


a = [3, 7, 5, 63, 111, 95]

print(solution(a))              # 결과 : [1, 1, 0, 1, 1, 0]