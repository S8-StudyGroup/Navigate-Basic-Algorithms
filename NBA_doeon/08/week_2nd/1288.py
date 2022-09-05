# 새로운 불면증 치료법

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())

    # 각 자리의 숫자를 저장하기 위한 셋 set_num 생성
    ## set을 쓰는 이유 : 양 N번의 각 자리의 숫자를 '순서 없이', '중복 없이' 저장하기 위함
    set_num = set()

    count = 1

    # set_num이 0 ~ 9로 이뤄질 때까지를 종료조건으로 하여 N의 자릿수 값 추가를 반복
    while set_num != {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:

        for num_element in str(num * count):  ## N을 자릿수 값으로 하나씩 떼어내기 위해 str함수 사용

            # 해당 자릿수 값이 set_num에 아직 없는 숫자일 때 set_num에 값 추가
            if num_element not in set_num:
                set_num.add(num_element)
            else:
                pass
        count += 1  ## N, 2N, 3N, ...

    print(f'#{test_case} {num * (count - 1)}')
    ## count - 1 인 이유 : set_num을 완성해도 count += 1하고
    # while을 빠져나오기 때문에 -1 처리를 해줌
