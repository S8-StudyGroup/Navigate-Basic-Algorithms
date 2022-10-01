# 숫자를 정렬하자

# 버블 정렬
for tc in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers) - 1, 0, -1): # 인접한 두 숫자 비교했을 때 오른쪽 게 더 작으면, 둘 순서를 바꿔준다!
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f'#{tc}', end=' ')            
    print(*numbers)