def solution(price, money, count):
    require = price * sum(range(1, count + 1))
    return max(0, require - money)

def solution(price, money, count):
    # 1부터 count까지의 합: count * (count + 1) // 2
    total_price = price * count * (count + 1) // 2
    return max(0, total_price - money)