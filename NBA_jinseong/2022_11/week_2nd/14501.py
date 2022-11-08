# [BOJ] 14501. 퇴사

# idea
# 전기버스 비스무리
# 해당 날짜 상담 기간을 저장하는 T, 금액 P
# 0~(N-1)까지 정보가 있음
# N이면 되면 끝

def max_price(day, price_sum):
    global max_result
    if day == N:  # 0부터 시작한 날짜가 N이 되면 끝냄
        if price_sum > max_result:
            max_result = price_sum
        return

    working_day = T[day]
    if day + working_day <= N:  # 퇴사날짜를 넘지않으면
        next_day = day + working_day  # 일 맡기
        max_price(next_day, price_sum + P[day])
    max_price(day + 1, price_sum)  # 일 안맡고 다음날 넘어가기


N = int(input())
T = []
P = []
max_result = 0
for i in range(N):
    time, price = map(int, input().split())
    T.append(time)
    P.append(price)

max_price(0, 0)

print(max_result)



