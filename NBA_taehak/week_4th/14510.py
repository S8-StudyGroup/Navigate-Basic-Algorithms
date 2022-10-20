# [SWEA] 14510. 나무 높이

for case_num in range(1, int(input()) + 1):
    tree_cnt = int(input())
    trees = list(map(int, input().split()))
    
    # 최대 높이랑 차이값 구하기
    max_height = max(trees)
    diffs = []
    for tree in trees:
        diffs.append(max_height - tree)
    
    min_odd_day = 0
    even_day = 0
    
    for diff in diffs:
        if diff % 2 != 0:
            min_odd_day += 1
        even_day += diff // 2
    
    bb = [0, 2, 3]
    day = 0
    if min_odd_day > even_day:
        day = min_odd_day * 2 - 1
    elif min_odd_day == even_day:
        day = min_odd_day * 2
    else:
        even_day -= min_odd_day
        normal = even_day // 3
        day_diff_0 = even_day % 3
        day += min_odd_day * 2 + normal * 4 + bb[day_diff_0]
    
    print(f'#{case_num} {day}')