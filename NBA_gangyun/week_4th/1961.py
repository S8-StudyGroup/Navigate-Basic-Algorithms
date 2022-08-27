# 숫자 배열 회전

for test_case in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(input().split()) for _ in range(N)]

    matrix_90 = []
    matrix_180 = []
    matrix_270 = []

    for j in range(N):
        rot = ''
        for i in range(N - 1, -1, -1):
            rot += matrix[i][j]
        matrix_90.append(rot)

    for i in range(N - 1, - 1, - 1):
        rot = ''
        for j in range(N - 1, -1, -1):
            rot += matrix[i][j]
        matrix_180.append(rot)

    for j in range(N - 1, - 1, - 1):
        rot = ''
        for i in range(N):
            rot += matrix[i][j]
        matrix_270.append(rot)

    new_matrix = [matrix_90] + [matrix_180] + [matrix_270]

    print(f'#{test_case}')
    for num in list(map(list, zip(*new_matrix))):
        print(*num)
