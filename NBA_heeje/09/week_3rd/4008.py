# [SWEA] 4008. 숫자 만들기

# from itertools import permutations


# 중복되는 숫자가 존재하는 순열 구하기
# cur_arr: 현재 누적 중인 연산자 리스트, oper_arr: 사용해야하는 연산자 리스트, n: 사용해야하는 연산자 개수
def make_permutations_overlapped_numbers(cur_arr, oper_arr, n):

    if n == 0:  # 모든 연산자를 사용하였다면
        operator_case.append(cur_arr)  # 현재까지 누적된 연산자 리스트를 따로 저장해준 뒤
        return  # 재귀를 빠져나온다.

    # 0: 더하기, 1: 빼기, 2: 곱하기, 3: 나누기
    for i in range(4):  # oper_arr 순환
        if oper_arr[i] != 0:  # 해당 연산자를 사용해야 한다면
            new_oper_arr = oper_arr[:]  # oper_arr 복사(중요!)
            new_oper_arr[i] -= 1  # 해당 연산자를 사용할 거니까 1 빼준다.

            # cur_arr에 해당 연산자 추가, new_oper_arr로 교체, 남은 연산자 개수에 1을 빼준 값으로 재귀
            make_permutations_overlapped_numbers(cur_arr + [i], new_oper_arr, n - 1)


# 0: 더하기, 1: 빼기, 2: 곱하기, 3: 나누기
operator_dict = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: x // y if x >= 0 else -(-x // y),
    # -2 // 3을 했을 때 원하는 값: -2, 실제 나오는 값: -1
    # Why? https://gksdudrb922.tistory.com/207
}
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    operator_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))

    # 시간 초과 케이스
    # 주어진 문제의 시간 : 50개 테케를 합쳐서 python의 경우 10초 (1문제당 약 0.2초(2천만번))
    # N = 12일 때 permutations(operators)는 총 11!(약 4천만번)의 연산을 하고,
    # list()와 set() 역시 안에 들어간 iterator의 길이만큼의 연산을 하므로
    # 약 1억 2천만번의 연산을 수행하기 때문에 시간 초과!

    # operators = []

    # for idx in range(4):
    #     operators.extend([idx] * operator_list[idx])  # 예) ['+', '+', '-', '/']
    # operator_case = list(set(permutations(operators)))

    operator_case = []
    make_permutations_overlapped_numbers([], operator_list[:], N - 1)

    maximum = -100000000  # 최댓값
    minimum = 100000000  # 최솟값

    for cal_operator in operator_case:
        temp = number_list[0]
        for i in range(N - 1):
            # 각 연산자에 대해 연산 수행
            temp = operator_dict[cal_operator[i]](temp, number_list[i + 1])

        if temp > maximum:  # 계산 값과 저장된 최댓값을 비교
            maximum = temp
        if temp < minimum:  # 계산 값과 저장된 최솟값을 비교
            minimum = temp
    print(f"#{tc} {maximum - minimum}")
