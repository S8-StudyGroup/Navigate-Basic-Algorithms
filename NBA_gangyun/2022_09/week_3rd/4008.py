# [SWEA] 4008. 숫자 만들기

calculator_list = ['+', '-', '*', '/']


def dfs(recent, check):
    if check == N - 1:
        calculators = recent
        new_num = num_list[0]
        for i in range(len(calculators)):
            if calculators[i] == '+':
                new_num += num_list[i + 1]
            elif calculators[i] == '-':
                new_num -= num_list[i + 1]
            elif calculators[i] == '*':
                new_num *= num_list[i + 1]
            else:
                new_num /= num_list[i + 1]
                new_num = int(new_num)

        result.append(new_num)
        return

    for i in range(4):
        if calculator_info[i] > 0:
            calculator_info[i] -= 1
            recent.append(calculator_list[i])
            dfs(recent, check + 1)
            recent.pop()
            calculator_info[i] += 1


for test_case in range(1, int(input()) + 1):
    N = int(input())
    calculator_info = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    result = []
    dfs([], 0)
    max_num = max(result)
    min_num = min(result)
    print(f'#{test_case} {max_num - min_num}')
