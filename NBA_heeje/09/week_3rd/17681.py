# [Programmers] 17681. [1차] 비밀지도


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        combine_row = arr1[i] | arr2[i]     # 비트 연산(or)
        decoding_row = ""                   # 해독된 행 암호

        for j in range(n - 1, -1, -1):      # 왼쪽부터 비교하기 위해 역순 탐색
            if combine_row & (1 << j):      # 해당 자릿수가 1이라면(벽)
                decoding_row += "#"         # 벽('#') 삽입
            else:                           # 해당 자릿수가 0이라면(공백)
                decoding_row += " "         # 공백(' ') 삽입

        answer.append(decoding_row)
    return answer
