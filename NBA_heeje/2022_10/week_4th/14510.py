# [SWEA] 14510. 나무 높이

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    tallest_tree = max(trees)
    is_odd = True if tallest_tree % 2 else False
    is_odd_list = [True if trees[i] % 2 else False for i in range(N)]
    day = 0
    while True:

        prev = trees[0]
        for i in range(1, N):
            if trees[i] != prev:
                break
        else:
            break

        day += 1

        # 홀수
        if day % 2:
            for i in range(N):
                if is_odd_list[i] != is_odd:
                    trees[i] += 1
                    is_odd_list[i] = is_odd
                    break
            else:
                shortest_tree_idx = -1
                shortest_tree = 121
                for idx, val in enumerate(trees):
                    if val < shortest_tree:
                        shortest_tree_idx = idx
                        shortest_tree = val
                if shortest_tree < tallest_tree - 2:
                    trees[shortest_tree_idx] += 1
                    is_odd_list[shortest_tree_idx] = not is_odd_list[shortest_tree_idx]
        else:
            shortest_tree_idx = -1
            shortest_tree = 121
            for idx, val in enumerate(trees):
                if val <= tallest_tree - 2:
                    trees[idx] += 2
                    break

    print(f"#{tc} {day}")
