# 1대1 가위바위보

# 1
A, B = map(int, input().split())

## 기본적으로 숫자가 크면 승
if A > B:
    ## 이때, 숫자 크기로 승패가 결정되는 상황의 예외(가위: 1, 보: 3)를 if로 케이스 분해
    if A == 3 and B == 1: 
        print('B')
    else:
	    print('A')
else:
    if A == 1 and B == 3:
        print('A')
    else:
        print('B')


# 2 위의 개념을 그대로 set 이용 
A, B = map(int, input().split())

## A와 B가 낸 값이 누가 되었든 (1, 3) 조합일 때 예외 발생하므로 따로 케이스 분해
if {A, B} == {1, 3}:
    if A > B:
        print('B')
    else:
        print('A')

## 나머지 케이스는 무조건 숫자가 크면 이김
else:
    if A > B:
        print('A')
    else:
        print('B')
