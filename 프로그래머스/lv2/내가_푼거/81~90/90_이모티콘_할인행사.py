from itertools import product

def solution(users, emoticons):
    discount = [9, 8, 7, 6]

    discount_rate_list = list(product(range(4), repeat=len(emoticons)))
    discount_rate_price = []

    for discount_rate in discount_rate_list :
        prices = []
        for emoticon, rate in zip(emoticons, discount_rate) :
            prices.append((rate, int(emoticon * discount[rate] // 10)))
        discount_rate_price.append(prices)

    for i, user in enumerate(users) :
        hope = user[0]
        if hope <= 10 :
            users[i][0] = 0
        elif hope <= 20 :
            users[i][0] = 1
        elif hope <= 30 :
            users[i][0] = 2
        else :
            users[i][0] = 3

    subscribe = 0
    income = 0

    for rate_price in discount_rate_price :
        cur_subscribe = 0
        cur_income = 0
        for hope_rate, budget in users :
            cost = 0
            for rate, price in rate_price :
                if rate >= hope_rate :
                    cost += price
            if cost >= budget :
                cur_subscribe += 1
            else :
                cur_income += cost
        if cur_subscribe > subscribe :
            subscribe = cur_subscribe
            income = cur_income
        elif cur_subscribe == subscribe and cur_income > income :
            income = cur_income

    return [subscribe, income]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
