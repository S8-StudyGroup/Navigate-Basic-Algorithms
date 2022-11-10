# [BOJ] 14501. 퇴사

def talk(i, gain=0):
    global max_gain

    # 현재 날의 상담을 끝낼 수 있을 때
    if i + plans[i] < n:
        talk(i + plans[i], gain + gains[i])

    # 현재 날 시작하는 상담을 하면 N일을 다 채울 때
    elif i + plans[i] == n:
        if gain + gains[i] > max_gain:
            max_gain = gain + gains[i]

    # 현재 날이 상담 마지막일 때, (현재 날부터 시작하는 상담은 수행하지 못함)
    else:
        if gain > max_gain:
            max_gain = gain

    # 현재 날짜를 포함하지 않고 다음 날로 건너뜀
    if i + 1 < n:
        talk(i + 1, gain)


n = int(input())
plans = []
gains = []
for _ in range(n):
    t, p = map(int, input().split())
    plans.append(t)
    gains.append(p)
max_gain = 0
talk(0)
print(max_gain)
