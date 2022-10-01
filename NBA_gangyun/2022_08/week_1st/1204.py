# 최빈수 구하기
T = int(input())

for test_case in range(1, T + 1):
    test_num = int(input())
    num_list = list(map(int, input().split()))
    check_num = []

    for i in range(len(num_list)):
        check_num.append(num_list.count(num_list[i]))

    num_dict = {num_list[i]: check_num[i] for i in range(len(num_list))}

    for key, value in num_dict.items():
        if value == max(num_dict.values()):
            print(f'#{test_num} {key}')
