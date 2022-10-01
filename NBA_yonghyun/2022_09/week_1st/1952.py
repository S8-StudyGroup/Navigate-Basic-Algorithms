# 1952. [모의 SW 역량테스트] 수영장

for test_case in range(1, int(input()) + 1):
    sub = list(map(int, input().split()))
    use = list(map(int, input().split()))

    print(sub)
    print(use)

    # 1일권 only
    day = 0
    for d in use:
        day += d * sub[0]
    print(day)

    # 1달권 only
    month = 0
    for m in use:
        if m != 0:
            month += sub[1]
    print(month)

    # 1년권 only
    year = sub[3]
    print(year)

    # 혼합
    big_three = 0
    pay = []
    for i in range(10):
        three = 0
        for j in range(3):
            three += use[i+j]
            pay.append(i + j)
        print(three)
        print(pay)
        if three > big_three:
            big_three = three
            pay = pay[-1:-4:-1]
        else:
            pay = pay[0:3]

    for i in pay:
        if sub[0] * use[i] >= sub[2]:

    print(pay)
