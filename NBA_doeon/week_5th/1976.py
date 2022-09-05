# 시각 덧셈

t = int(input())

for tc in range(1, t + 1):
    a_h, a_m, b_h, b_m = map(int, input().split())
    
    hour = (a_h + b_h) % 12
    hour += (a_m + b_m) // 60

    minute = (a_m + b_m) % 60
    
    
    print(f'#{tc} {hour} {minute}')