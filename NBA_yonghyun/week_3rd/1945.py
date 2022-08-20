# 간단한 소인수분해

'''
[ 아이디어 ]

소수 담은 리스트 

5번 for문 반복

나눴을 때 0이 아닐때까지 while문 돌도록 함
카운트 +

각각의 결과를 리스트에 넣고

언패킹하여 출력

'''


pn = [2, 3, 5, 7, 11]

t = int(input())

for test_case in range(1, t + 1):

    number = int(input())

    c_num_list = []

    for n in pn:

        c_num = 0  # 소수 카운트

        while True:
            if number % n == 0:
                c_num += 1
                number = number // n

            else:
                break

        c_num_list.append(c_num)

    print(f'#{test_case}', *c_num_list)
