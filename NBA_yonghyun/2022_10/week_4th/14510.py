# [SWEA] 14510. 나무 높이


# 나무 물주기 pass 코드


for tc in range(1, int(input()) + 1):

    n = int(input())
    tree_height = list(map(int, input().split()))
    tree_height.sort()  # 트리 높이를 정렬해줌

    max_h = tree_height[-1]  # 마지막 높이가 최대 높이

    for i in range(n):  # 트리 높이 리스트를 최대 높이에서 현재 높이를 뺀 값으로 만듦
        tree_height[i] = max_h - tree_height[i]
    # print(tree_height)

    tree_two = 0
    tree_one = 0
    for tree in tree_height:  # 각 트리 높이에 대한 처리
        while tree > 0:
            if tree % 2 == 0:  # 트리 높이를 2로 나눌 수 있으면, tree_two 카운트
                tree -= 2
                tree_two += 1
            else:  # 트리 높이를 2로 나눌 수 없으면, tree_one 카운트
                tree -= 1
                tree_one += 1

    # print('two', tree_two)
    # print('one', tree_one)
    day = 0

    if tree_two == tree_one:  # tree_two 와 tree_one 의 개수가 같으면
        day = tree_one * 2  # 두 트리 개수 더한 것과 최소 소요 날짜가 같음

    elif tree_two > tree_one:  # tree_two 가 더 많으면, (tree_two 는 쪼갤 수 있음)
        k = (tree_two - tree_one) * 2
        d = 0
        while k > 1:  # 쪼개는 과정 진행
            d += 1
            if d % 2 != 0:  # 홀수날
                k -= 1
            else:  # 짝수날
                k -= 2
        if k > 0:
            d += 1

        # print('a', d)
        day = tree_one * 2 + d

    else:  # tree_one 이 더 많으면, (tree_one 은 합칠 수 없음)
        day = tree_one * 2 - 1  # 짝수번째 날은 비운 채로 진행해야 함

    print(f'#{tc} {day}')
