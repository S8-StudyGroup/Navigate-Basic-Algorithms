# 두 개의 숫자열

# 테스트 케이스의 개수
T = int(input())

# 각 테스트 케이스
for test_case in range(1, T + 1):

    # a, b 입력받아 저장
    a, b = map(int, input().split())

    # a, b에 대응하는 리스트 생성
    long_list = list(map(int, input().split()))
    short_list = list(map(int, input().split()))
    answer = -999999

    # 길이가 더 긴 쪽을 a, long_list에 삽입
    if a < b:
        a, b = b, a
        long_list, short_list = short_list, long_list

    # 이중 for문을 통해 마주보는 숫자를 곱한 뒤 모두 더한 값의 최댓값을 구함
    for i in range(a - b + 1):
        sum = 0
        for j in range(len(short_list)):
            sum += long_list[i + j] * short_list[j]
        if answer < sum:
            answer = sum

    print(f"#{test_case} {answer}")
