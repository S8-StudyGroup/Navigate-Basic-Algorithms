# 숫자 배열 회전


def rotate(a, size):
    result = ['' for _ in range(size)]

    for i in range(size - 1, -1, -1):
        for j in range(size):
            result[j] += a[i][j]

    return result


for case in range(1, int(input()) + 1):

    # 행렬 크기
    size = int(input())

    # 행렬
    arr = [input().replace(' ', '') for _ in range(size)]

    result1 = rotate(arr, size)

    result2 = rotate(result1, size)

    result3 = rotate(result2, size)

    result = [result1, result2, result3]

    print(f'#{case}')
    for i in range(size):
        print(result1[i], result2[i], result3[i])
