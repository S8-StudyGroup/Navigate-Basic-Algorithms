# [BOJ] 2502. 떡 먹는 호랑이

day, cake_cnt = map(int, input().split())

# a[day] + b[day] = cake_cnt ; 
a = [0, 1, 0]
b = [0, 0, 1]

day_0 = 3
while day_0 <= day:

    a.append(b[-1])
    b.append(b[-2] + b[-1])

    day_0 += 1

a_ratio = a[-1]
b_ratio = b[-1]

A = 1
while True:
    B_b_ratio = cake_cnt - A * a_ratio
    if B_b_ratio % b_ratio == 0:
        B = B_b_ratio // b_ratio
        break
    A += 1

print(A)
print(B)