# 2635. 수 이어가기

first_num = int(input())
max_cnt = 0             # 최대 이어진 횟수 초기값
max_cnt_record = []     # 최대 이어진 수열 초기값

for second_num in range(1, first_num + 1):  # 두번째 숫자로 가능한 경우(1 ~ 입력 숫자)
    cnt = 0                                 # 이어진 횟수 초기화
    cnt_record = []                         # 이어진 수열 초기화
    f = first_num                           # first_num을 가져옴 (이게 없으면 for문 돌다가 전에 바뀌어진 first_num 값이 반영돼서 안 됨)
    breaker = False                         # breaker 초기값 (멈추게 할 경우 실행되도록 함)

    while breaker == False:
        if f - second_num >= 0:                         # 1) 뺀 값이 0보다 크거가 같을 때에만
            cnt_record.append(second_num)               # 뒷 숫자를 이어진 수열에 append하고
            cnt += 1                                    # 이어진 횟수를 한 번 더함
            f, second_num = second_num, f - second_num  # 앞, 뒤 숫자를 업데이트
        else:                                           # 2) 뺀 값이 음수가 나올 경우
            cnt_record.append(second_num)               # 뒷 숫자를 이어진 수열에 append하고
            cnt += 1                                    # 이어진 횟수를 한 번 더한 뒤
            breaker = True                              # while문을 빠져나감

    # 매 second_num마다 해당 cnt가 현재 최대값보다 큰지 검사하고 업데이트
    if cnt > max_cnt:
        max_cnt = cnt
        max_cnt_record = cnt_record

print(max_cnt + 1)  # 첫 번째 입력값은 이어진 수에 포함되지 않았으므로 + 1 따로 해줌
print(first_num, *max_cnt_record)
