# 수도 요금 경쟁
Test_count = int(input())
for i in range(Test_count):
    P, Q, R, S, W = map(int, input().split(" "))
    A_water_fee = P * W
    B_water_fee = Q if R > W else Q + S * (W - R)
    print(f"#{i + 1}", A_water_fee if A_water_fee < B_water_fee else B_water_fee)
