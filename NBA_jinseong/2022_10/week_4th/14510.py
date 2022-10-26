# [SWEA] 14510. 나무 높이
# 미해결


for t in range(1, int(input()) + 1):
    N = int(input())
    heights = list(map(int, input().split()))

    max_height = max(heights)

    time_grow = 0

    for height in heights:
        time_grow += max_height - height

    result = 0
    if time_grow <= 2:
        result = time_grow
    elif time_grow > 2:
        result += (time_grow // 3) * 2
        rest_time = time_grow % 3
        result += rest_time

    print(f'#{t} {result}')
