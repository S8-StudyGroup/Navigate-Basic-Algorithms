# [SWEA] 14510. 나무 높이

# 문제 핵심
# a. 홀수 번째 날은 1, 짝수 번째 날은 2만큼 키가 자란다.
# b. 모든 나무의 키가 처음에 가장 키가 컸던 나무와 "같아져야 한다".
# c. 어떤 날에는 물을 주지 않을 수도 있다.

# 아이디어
# 1. BFS, DFS?
#   - BFS : 너비우선탐색으로 해결할 수 있을 만한 방안이 보이지 않음!
#   - DFS : 다른 나무에 물을 주는 것을 가지로 나누어 줄 필요가 없어보임! (완전탐색x)

# 2. 어떻게 풀까?
# 홀수 번째 날과 짝수 번째 날마다 우선적으로 물을 줘야 하는 나무의 기준을 정해보자.

# 2-1. 홀수 번째 날
# 우선순위1 : 처음에 가장 키가 컸던 나무와 홀짝이 다른 나무에게 먼저 물을 주자!
# 이유 : 1을 더했을 때만 홀짝 변경이 가능하다. 2를 더했을 때는 할 수 없는 일
# 우선순위2 : 가장 키가 작은 나무에게 물을 주자! 단, 홀수 번째 날에 물을 주지 않고
#           짝수 날에 주는 게 더 빠를 땐 주지 않는다.

# 2-2. 짝수 번째 날
# 나무리스트를 순회하여 가장 키가 컸던 나무와 비교했을 때 키 차이가 2 이상이면 물을 준다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    tallest_tree = max(trees)                       # 가장 키가 큰 나무
    is_odd = True if tallest_tree % 2 else False    # 가장 키가 큰 나무의 홀짝 여부
    day = 0                                         # 날짜 수

    # 나무들의 홀짝 여부 표시
    is_odd_list = [True if trees[i] % 2 else False for i in range(N)]

    while True:

        # 모든 나무들의 키가 같다면 while문 탈출
        # 처음부터 키가 모두 같은 경우를 위해 위쪽에 배치
        prev = trees[0]
        for i in range(1, N):
            if trees[i] != prev:
                break
        else:
            break

        day += 1                                    # 하나라도 키가 다르다면 day + 1

        if day % 2:                                 # 홀수 번째 날일 때
            for i in range(N):
                if is_odd_list[i] != is_odd:        # 가장 큰 나무의 홀짝 여부와 비교
                    trees[i] += 1                   # 다르다면 물을 준다.
                    is_odd_list[i] = is_odd         # 해당 나무 홀짝 변경
                    break
            else:                                   # 모두 홀짝이 같다면
                shortest_tree_idx = -1              # 가장 키가 짧은 나무의 인덱스
                shortest_tree = 121                 # 가장 키가 짧은 나무의 키
                cnt = 1                             # 가장 키가 짧은 나무의 개수

                # 가장 키가 짧은 나무 구하기
                for idx, val in enumerate(trees):
                    if val < shortest_tree:
                        shortest_tree_idx = idx
                        shortest_tree = val
                        cnt = 1
                    elif val == shortest_tree:      # 가장 키가 짧은 나무가 여러개이면
                        cnt += 1                    # cnt + 1

                # 만약 가장 키가 짧은 나무의 키차이가 2이며 그 나무의 개수가 1개라면 물을 주지 않음!!
                # 그렇지 않다면 가장 키가 짧은 나무에 물을 주고 해당 나무 홀짝 변경
                if not (shortest_tree == tallest_tree - 2 and cnt == 1):
                    trees[shortest_tree_idx] += 1
                    is_odd_list[shortest_tree_idx] = not is_odd_list[shortest_tree_idx]

        # 짝수일 때
        else:
            for idx, val in enumerate(trees):       # 트리 리스트를 순회하여
                if val <= tallest_tree - 2:         # 해당 나무의 키차이가 2 이상이라면
                    trees[idx] += 2                 # 물을 준다!
                    break

    print(f"#{tc} {day}")
