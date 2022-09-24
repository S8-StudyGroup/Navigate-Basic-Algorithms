# [SWEA] 4008. 숫자 만들기
# Guest - 김진호

# 2. 이전까지 합산값, 계산위치, 사용된후 연산자 개수를 받을 sol함수 작성
def sol(total, idx, ops):

    # 2_1 재귀의 마지막 지정. 모든 연산을 마친 이후이기때문에 idx == N
    #     재귀의 마지막에서 max,min값을 확인.
    if idx == N:
        global max_cal, min_cal
        if total > max_cal:
            max_cal = total
        if total < min_cal:
            min_cal = total
        return

    # 2_2 연산자 개수를 확인하고 한단계씩 연산을 하고 재귀함수를 호출하는 반복문 생성
    for op_idx in range(4):  # (1) 연산자 개수가 담긴 ops의 배열 크기는 4이므로 0~3까지 탐색
        if ops[op_idx]:  # (2) 해당 자리가 0이 아니라면 아래 실행 (0이면 다음자리로)
            if op_idx == 0:
                next_total = total + nums[idx]
            elif op_idx == 1:
                next_total = total - nums[idx]
            elif op_idx == 2:
                next_total = total * nums[idx]
            else:
                next_total = int(
                    total / nums[idx]
                )  # (3) 연산자 기호에 따라 계산하기. 나눗셈일 경우 소수점 버리기
            ops[op_idx] -= 1  # (4) 다음 재귀함수 호출을 위해 이번에 사용한 연산자 개수 1 줄이기
            sol(next_total, idx + 1, ops)  # (5) 지금까지 계산한 값, 다음 인덱스값, 연산자 리스트로 재귀함수 호출
            ops[op_idx] += 1  # (6) 재귀 종료시 다시 값 채워주기 (해당 연산자를 사용하지 않는 경우도 고려)

        # if ops[op_idx]:                                       # 위와 같은식. next_total 변수를 없앤 버전
        #     ops[op_idx] -= 1                                  # 재귀함수 호출 위치 변동에 따라, 위의 (4)번 과정 위로 올리기
        #     if op_idx == 0:
        #         sol(total + nums[idx], idx + 1, ops)
        #     elif op_idx == 1:
        #         sol(total - nums[idx], idx + 1, ops)
        #     elif op_idx == 2:
        #         sol(total * nums[idx], idx + 1, ops)
        #     else:
        #         sol(int(total / nums[idx]), idx + 1, ops)     # next_total을 지정하지않고, 즉시 계산해서 재귀호출
        #     ops[op_idx] += 1


# 1. 입력받을 main 파트

# 1_1. 입력받을 값 입력받기
for test_case in range(1, int(input()) + 1):
    N = int(input())
    cals = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    # 1_2. 문제에서 주어진 최대값, 최소값으로 최대,최소값 지정
    max_cal = -100000000
    min_cal = 100000000

    # 1_3 sol()에 nums 처음값과 1번 인덱스값, 그리고 연산자 초기값을 넣어서 실행
    sol(nums[0], 1, cals)

    # 1_4 출력은 최대,최소의 차이이기때문에 해당 값으로 출력
    print(f'#{test_case} {max_cal-min_cal}')
