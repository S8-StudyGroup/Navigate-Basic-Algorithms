# 숫자를 정렬하자
import sys

sys.stdin = open("input")


def bublle_sort(a):  # a == 정렬해야될 list
    for x in range(len(a)-1, 0, -1):
        for y in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                    # 파이선 식으로 바꿔준다.

    return a


t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    data = list(map(int, input().split()))
    # 버블정렬을 활용해서 정렬을 한다.
    for i in range(n - 1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    print(f"#{tc}", *data)
    print()
    a = bublle_sort(data)
    print(f"#{tc}", *a)