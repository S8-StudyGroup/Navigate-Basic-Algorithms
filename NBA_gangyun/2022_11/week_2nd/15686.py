# BOJ_15686. 치킨 배달


def chicken_combo(start, end):
    global min_distance

    # 조합의 개수가 채워지면 if문으로 들어감
    if len(picked_bbq) == end:
        chicken_distance = 0

        # 맨해튼 거리 구하기
        for i in range(city_size):
            for j in range(city_size):
                if city_info[i][j] == 1:
                    distance_list = []
                    for (bbq_i, bbq_j) in picked_bbq[:]:
                        m_d = abs(bbq_i - i) + abs(bbq_j - j)
                        distance_list.append(m_d)
                    chicken_distance += min(distance_list)
                    if chicken_distance > min_distance:
                        break

        # 백트래킹
        if chicken_distance < min_distance:
            min_distance = chicken_distance

    # 조합을 구하는 반복문
    for i in range(start, len(bbq_list)):
        picked_bbq.append(bbq_list[i])
        chicken_combo(i + 1, end)
        picked_bbq.pop()


# 변수 초기화
city_size, alive_BBQ = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(city_size)]
bbq_list = []
picked_bbq = []
min_distance = 100 * 13

# 치킨집의 좌표를 bbq_list에 저장
for i in range(city_size):
    for j in range(city_size):
        if city_info[i][j] == 2:
            bbq_list.append((i, j))

# 치킨집의 조합에 따라 맨해튼거리를 구하면서 비교
chicken_combo(start=0, end=alive_BBQ)

print(min_distance)
