# [Programmers] 17681. [1차] 비밀지도

def solution(n, arr1, arr2):
    map_arr1 = list([0] * n for _ in range(n))
    map_arr2 = list([0] * n for _ in range(n))
    answer = []
    for index, i in enumerate(arr1):
        a = format(i, 'b')

        while len(a) < n:
            a = str(0) + str(a)
            if len(a) == n:
                map_arr1[index] = list(a)
                break
        else:
            map_arr1[index] = list(a)

    for index, j in enumerate(arr2):
        b = format(j, 'b')

        while len(b) < n:
            b = str(0) + str(b)
            if len(b) == n:
                map_arr2[index] = list(b)
                break
        else:
            map_arr2[index] = list(b)

    for i in range(n):
        tmp = ''
        for j in range(n):
            if map_arr1[i][j] == '1' or map_arr2[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer


n1 = 5
arr3 = [9, 20, 28, 18, 11]
arr4 = [30, 1, 21, 17, 28]


print(solution(n1, arr3, arr4))