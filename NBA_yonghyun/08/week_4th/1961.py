# 숫자 배열 회전

'''
저번 수업 때 다뤘던 문제
zip 함수 사용하면 쉽게 풀 수 있음
'''

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = [input().replace(' ', '') for _ in range(n)]

    # 90도
    arr2 = list(map(''.join, zip(*arr)))

    # 180도
    arr3 = [arr[i][-1::-1] for i in range(n - 1, -1, -1)]

    # 270도
    arr4 = list(map(''.join, zip(*arr3)))

    print(f'#{test_case}')
    for i in range(n):
        print(arr2[i][::-1], arr3[i], arr4[i][::-1])
