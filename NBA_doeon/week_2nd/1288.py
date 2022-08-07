# 새로운 불면증 치료법

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())

    set_num = set()
    count = 1
    while set_num != {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
 
        for num_element in str(num * count):
            if num_element not in set_num:
                set_num.add(num_element)
            else:
                pass
        count += 1
        
    print(f'#{test_case} {num * (count - 1)}')