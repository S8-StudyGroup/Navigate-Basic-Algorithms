# [Programmers] 17681. [1차] 비밀지도


def solution(n, arr1, arr2):
    '''
    n: 정사각형의 크기
    arr1: 지도 1의 정보
    arr2: 지도 2의 정보
    answer: 지도 1과 지도 2를 합해서 #으로 출력
    '''
    answer = []

    for i in range(n):
        row = ''
        for j in range(n - 1, -1, -1):
            if arr1[i] & (1 << j) or arr2[i] & (1 << j):
                row += '#'
            else:
                row += ' '
        answer.append(row)

    return answer


def solution2(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:]
        row = ' ' * (n - len(row)) + row
        row = row.replace('0', ' ')
        answer.append(row.replace('1', '#'))

    return answer


# test

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
print(solution2(n, arr1, arr2))
