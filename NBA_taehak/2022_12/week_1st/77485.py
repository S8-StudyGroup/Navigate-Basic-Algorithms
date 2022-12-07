# [Programmers] 77485. 행렬 테두리 회전하기
from collections import deque

def idxes(command):
    '''
    query에 대응
    시계방향 순서로 idx 전부 반환
    '''
    answer = []
    sr, sc, er, ec = command

    for c in range(sc, ec + 1):
        answer.append((sr, c))

    for r in range(sr + 1, er + 1):
        answer.append((r, ec))

    for c in range(ec - 1, sc - 1, - 1):
        answer.append((er, c))

    for r in range(er - 1, sr, - 1):
        answer.append((r, sc))
    
    return answer


def solution(rows, columns, queries):
    answer = []

    # area 생성, (0행, 0열은 0), index를 1부터 사용하기위해(입력된 queries 그대로 쓰기위해)
    area = [[0]*columns, list(range(columns + 1))]
    for _ in range(rows - 1):
        plus = list(map(lambda x : x + columns, area[-1]))
        plus[0] = 0
        area.append(plus)

    # query 하나씩 불러와서
    for query in queries:

        # 변경해줄 곳 idx를 전부 가져옴 => idx_list
        idx_list = idxes(query)

        # idx_list로 해당하는 숫자를 불러와서 회전, 최소값은 answer에 더하고
        nums = deque()
        for r, c in idx_list:
            nums.append(area[r][c])
        nums.rotate(1)
        answer.append(min(nums))

        # idx_list에 그대로 넣기
        for r, c in idx_list:
            area[r][c] = nums.popleft()

    return answer