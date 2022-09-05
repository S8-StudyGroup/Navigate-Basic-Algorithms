# 숫자 배열 회전

tc = int(input())

for i in range(tc):
    N = int(input())

    matrix = [0] * N                                                ## ex) matrix = [0, 0, 0, 0, ....] 길이 N인 리스트

    for j in range(N):
        matrix[j] = input().replace(' ', '')                        ## 공백을 지운 문자열로 받기 ex) '1 2 3' 인경우 '123'

    matrix_90 = [0] * N                                             ##90도 회전한 행렬을 담을곳
    matrix_180 = [0] * N                                            ## 180도
    matrix_270 = [0] * N                                            ## 270도

    for k in range(N):                                              ## 규칙 ex) matrix = ['123', '456', '789'] 일때
        matrix_90[k] = [matrix[p][k] for p in range(N-1, -1, -1)]   ##  7,4,1  가져오고 8,5,2, 가져오고 9,6,3

    for k in range(N):
        matrix_180[k] = [matrix_90[p][k] for p in range(N-1, -1, -1)]

    for k in range(N):
        matrix_270[k] = [matrix_180[p][k] for p in range(N-1, -1, -1)]

    print(f'#{i + 1}')

    for k in range(N):
        print(*matrix_90[k], end=' ', sep='')                       ##90도 짜리 한줄,  180도 짜리 한줄 270도 짜리 한줄 출력
        print(*matrix_180[k], end=' ', sep='')
        print(*matrix_270[k], sep='')

