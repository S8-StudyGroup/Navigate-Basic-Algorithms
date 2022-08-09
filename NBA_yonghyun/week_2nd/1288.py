# 새로운 불면증 치료법

T = int(input())

for test_case in range(1, T + 1):

    # 0부터 9까지 담은 리스트 생성
    zero_to_nine = list(range(0, 10))

    N = int(input())
    k = 0

    # zero_to_nine 리스트가 빌 때까지 시행 (== 0부터 9까지 숫자가 다 나올 때까지)
    while len(zero_to_nine)!=0:
        k += 1
        num_each = []

        # kN번 양에 들어있는 숫자들을 num_each 리스트에 담음
        for i in str(k * N):
            num_each.append(i)
        
        # num_list에 들어있는 숫자가 zero_to_nine에 있으면 그 값을 제거
        for n in num_each:
            if int(n) in zero_to_nine:
                zero_to_nine.remove(int(n))
        

    print(f'#{test_case} {k * N}')
