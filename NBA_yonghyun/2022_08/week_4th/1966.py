# 숫자를 정렬하자

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    nums = list(map(int, input().split()))

    for _ in range(n):
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    print(f'#{test_case}', *nums)
