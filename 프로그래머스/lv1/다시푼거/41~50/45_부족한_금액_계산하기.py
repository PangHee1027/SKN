def solution(price, money, count):
    return max(price * sum(range(1, count + 1)) - money, 0)