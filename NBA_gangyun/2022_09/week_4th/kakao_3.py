from itertools import product


def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    purpose_list = []
    for combs in product(discount, repeat=len(emoticons)):

        discounted_price_list = []
        for i in range(len(emoticons)):
            discounted_price_list.append(round(emoticons[i] * (100 - combs[i]) / 100))

        money_list = []
        register = 0
        for user in users:
            money = 0
            for i in range(len(emoticons)):
                if combs[i] >= user[0]:
                    money += discounted_price_list[i]

            if money >= user[1]:
                register += 1
                money = 0

            money_list.append(money)
        purpose = [register, sum(money_list)]
        purpose_list.append(purpose)

    purpose_list.sort(key=lambda x: (x[0], x[1]))
    answer = purpose_list[-1]
    return answer


users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
discount = [10, 20, 30, 40]

print(solution(users, emoticons))