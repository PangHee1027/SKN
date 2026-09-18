def solution(price, money, count) :
    require = price * sum(range(0, count + 1))
    return (require - money) if require > money else 0
# print(solution(3, 20, 4))