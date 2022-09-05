# 숫자를 정렬하자

for case in range(1, int(input()) + 1):
    size = int(input())
    nums = list(map(int, input().split()))

    for i in range(size - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(f'#{case}', *nums)
