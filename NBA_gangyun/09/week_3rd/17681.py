# [Programmers] 17681. [1차] 비밀지도

def decimal_to_binary(num, map_size):
    binary_num = ''
    while len(binary_num) != map_size:
        if num != 0:
            if num % 2:
                binary_num += '1'
            else:
                binary_num += '0'
            num //= 2
        else:
            binary_num += '0'

    return binary_num[::-1]


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        new_binary_num = ''
        binary_num1 = decimal_to_binary(arr1[i], n)
        binary_num2 = decimal_to_binary(arr2[i], n)

        for j in range(n):
            if binary_num1[j] == '1' or binary_num2[j] == '1':
                new_binary_num += '#'
            else:
                new_binary_num += ' '

        answer.append(new_binary_num)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
