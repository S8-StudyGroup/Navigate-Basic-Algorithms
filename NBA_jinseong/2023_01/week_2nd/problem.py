# [BOJ] 15686. 치킨 배달
# 실패

# 남을 수 있는 최대 치킨집 수 : M
# 1 <= 집의 개수 <= 2N
# M <= 치킨집 <= 13

# 현재 치킨 집 수 확인
# 1.
# (현재 치킨 집 수) combination (M) -> 각 상황에서 치킨 거리 계산
# 2.

def after_closure(opened_chicken, num_to_opened):
    global city_chi_d
    if len(opened_chicken) == M:        # 치킨 거리 계산
        for i, j in normal_houses:
            house_chi_d = N
            for x, y in opened_chicken:
                d = abs(x - i) + abs(y - j)
                if d < house_chi_d:
                    house_chi_d = d
            city_chi_d += house_chi_d
        return

    if num_to_opened >= M:
        return
    opened_chicken.append(chicken_houses[num_to_opened])
    after_closure(opened_chicken, num_to_opened + 1)
    opened_chicken.pop()

    after_closure(opened_chicken, num_to_opened + 1)


N, M = map(int, input().split())
city = []
chicken_houses = []
normal_houses = []
for i in range(N):
    line = list(map(int, input().split()))
    city.append(line)
    for j in range(N):
        point = line[j]
        if point == 2:
            chicken_houses.append([i, j])
        elif point == 1:
            normal_houses.append([i, j])

city_chi_d = 0
after_closure([], 0)

print(city_chi_d)




