# [Programmers] 17681. [1차] 비밀지도


def solution(n, arr1, arr2):
    whole_map = []
    for i in range(n):
        whole_map.append(arr1[i] | arr2[i])   # or 비트연산

    answer = []
    for i in range(n):
        binary = bin(whole_map[i])[2:n+2]               # 0b010000 에서 0b 빼기
        if len(binary) != n:
            binary = '0' * (n - len(binary)) + binary   # 자릿수 맞춰주기
        answer.append(binary.replace('1', '#').replace('0', ' '))

    return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))