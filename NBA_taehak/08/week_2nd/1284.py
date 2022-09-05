# 수도 요금 경쟁
'''
P : A사 1L당 요금
Q : B사 R리터 이하 요금 
S : B사 1L당 요금
W : 사용한 수도의 양 W리터
'''
import sys

sys.stdin = open('input_1284.txt')

for case in range(1, int(input()) + 1):
    a_rent, b_baserent, b_base, b_rent, my_water = map(int, input().split())

    # A사 수도요금
    choose_a = my_water * a_rent

    # B사 수도요금
    extra_water = my_water - b_base
    if extra_water <= 0:
        choose_b = b_baserent
    else:
        choose_b = b_baserent + extra_water * b_rent

    print(f'#{case} {min(choose_a, choose_b)}')
