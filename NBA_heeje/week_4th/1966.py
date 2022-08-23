# 숫자를 정렬하자

# 1. 버블 정렬 사용
# 시간 복잡도 : O(N^2)
# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))

#     for j in range(N - 1, 0, -1):
#         for i in range(j):
#             if numbers[i] > numbers[i + 1]:
#                 numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

#     print(f"#{tc}", *numbers)

# 2. sorted 사용 (권장)
# sorted -> 병합 정렬
# 최악의 경우에도 O(NlogN)의 시간 복잡도를 보장한다.
# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     print(f'#{test_case}',*sorted(map(int, input().split())))

# 3. 카운팅 정렬 사용
# 시간복잡도가 O(N + k)로 가장 낮지만, 정수 또는 정수로 표현할 수 있는 자료에 대해서만 적용 가능
# 집합 내의 가장 큰 정수를 알아야 한다. 상황에 따라 비효율적일 수 있음!!

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = max(numbers)
    c = [0] * (max_num + 1)
    sorted_numbers = []

    for number in numbers:
        c[number] += 1

    for i in range(len(c)):
        while c[i]:
            sorted_numbers.append(i)
            c[i] -= 1

    print(f"#{tc}", *sorted_numbers)
