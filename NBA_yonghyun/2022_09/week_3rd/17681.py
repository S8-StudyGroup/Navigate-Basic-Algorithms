# [Programmers] 17681. [1차] 비밀지도

'''
아이디어

1. 각 행을 십진수로 받은 암호를 이진수로 변환 (#, ""으로 변환한 지도 반환)
2. 두 지도의 크기는 같으므로, 같은 자리를 비교하여 최종 지도 반환
3. 최종 반환값의 형태는 리스트 내에 각 행이 하나의 문자열로 이루어져있음

예제
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
출력 = ["#####","# # #", "### #", "# ##", "#####"]
'''


def solution(n, arr1, arr2):

    table1 = code(n, arr1)  # 지도1
    table2 = code(n, arr2)  # 지도2

    answer = [""] * n

    for i in range(n):
        for j in range(n):
            if table1[i][j] == "#" or table2[i][j] == "#":  # 하나라도 벽
                answer[i] += "#"
            else:  # 모두 공백
                answer[i] += " "

    return answer


def code(n, arr):
    table = []  # "#"과 ""로 표현되는 지도

    for i in range(n):
        col = [0] * n  # 지도의 각 행
        num = arr[i]  # 입력 받은 십진수
        k = 0  # 이진수 저장할 리스트의 인덱스 번호
        for j in range(n - 1, -1, -1):  # 범위 : n-1 부터 0까지
            if num >= 2**j:  # 현재 숫자가 2의 j 제곱보다 크면 해당 자리의 이진수는 1
                num -= 2**j  # 현재 숫자 재조정
                col[k] = "#"
            else:
                col[k] = ""
            k += 1

        table.append(col)
    return table


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))
