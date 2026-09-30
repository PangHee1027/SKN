# 런타임 에러

def solution(n):
    root_five = 5 ** 0.5
    a = 1 / root_five
    b = ((1 + root_five) / 2) ** n
    c = ((1 - root_five) / 2) ** n
    return int(a * (b - c)) % 1234567
print(solution(5))