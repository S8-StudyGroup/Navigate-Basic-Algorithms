# [SWEA] 14510. 나무 높이
# Guest - 전동준

import sys

sys.stdin = open('Sample_input.txt')
# sys.stdin = open('debug.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())  # 나무 개수
    trees = list(map(int, input().split()))  # 나무 상태

    max_height = max(trees)  # 나무의 최대 길이(성장 목표)
    odd = 0  # 물을 1 더 줘야 하는 나무의 수
    even = 0  # 물을 2 더 줘야 하는 나무의 수

    day = 0  # 총 소요 기간

    # 내림차순 정렬
    trees.sort(reverse=True)

    # 모든 나무의 높이가 max_height가 될 때까지 반복
    while trees.count(max_height) < n:
        day += 1
        water = 1 if day % 2 == 1 else 2
        need_even = []  # 물이 2가 필요한 인덱스 번호

        for i in range(n):
            # 물을 1만큼 줄 수 있는데 필요한 물이 정확히 2인 경우
            if trees[i] + 2 == max_height and water == 1:
                need_even.append(i)
            # 그 외의 경우
            elif trees[i] + water <= max_height:
                trees[i] += water
                break

        # break에 걸리지 않고 모든 나무를 체크한 경우
        # 물이 1만큼 필요한 나무들만 남은 경우와 구분
        else:
            # 물이 2만큼 더 필요한 나무들만 남은 경우
            if need_even:
                even = len(need_even)

                # 물 2를 줘야 하는 나무에 1씩 두 번 주기
                odd = 0
                while abs(even - odd) > 1:
                    even -= 1
                    odd += 2

                # 추가로 필요한 날짜 보정 : while 구문에서 이미 한 번 더했음을 고려
                addition_day = 0 if odd > even else 1
                day += min(odd, even) + addition_day
                break

    print(f'#{tc}', day)

# 보충 : 날짜 보정 알고리즘(for-else의 else 부분) 도출 과정

# 1개면 +2 1회
# 2
# 0 - 2

# 2개면 +1 2회, +2 1회
# 2 /  2
# (1, 1) / 2
# 1 - 2 - 1

# 3개면 +1 2회, +2 2회
# (1, 1) / 2 / 2
# 1- 2 - 1 - 2

# 4개면 +1 2회, +2 3회
# 2 / 2 / 2 / 2
# (1, 1) / 2 / 2 / 2
# 1 - 2 - 1 - 2 - 0 - 2

# 5개면 +1 4회, +1 3회
# 2 / 2 / 2 / 2 / 2
# (1, 1) / 2 / (1, 1) / 2 / 2
# 1 - 2 - 1 - 2 - 1 - 2 - 1

# 6개면 +1 4회, +2 4회
# (1, 1) / 2 / (1, 1) / 2 / 2 / 2
# 1 - 2 - 1 - 2 - 1 - 2 - 1 - 2

# 7개면 +1 4회, +2 5회
# 2 / 2 / 2 / 2 / 2 / 2 / 2
# (1, 1) / 2 / (1, 1) / 2 / 2 / 2 / 2
# 1 - 2 - 1 - 2 - 1 - 2 - 1 - 2 - 0 - 2
