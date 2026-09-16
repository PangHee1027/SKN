def solution(sides):
    # 이건 좀 많이 수학적인데, a=(max(sides)) >= b=(min(sides)) 일 때 삼각형을 이루는 나머지 한변을 찾는 방법
    # 1. a가 가장 긴 변일 때 : a < b + x -> x > a - b
    # 이때 x <= a 이므로 x의 범위 -> a - b < x <= a
    # 2. x가 가장 긴 변일 때 : x < a + b
    # x의 범위 a <= x < a + b
    # 1, 2를 정리하면 a - b < x < a + b
    # a - b, a + b 사이의 정수 = (a + b - 1) - (a - b + 1) + 1
    # a + b = sum(sides), a = max(sides), b = min(sides)
    # 대입하면 (sum - 1) - (max - min + 1) + 1 = sum - max + min - 1
    # 이와 별개로 2b - 1 = min * 2 - 1 도 가능
    return sum(sides) - max(sides) + min(sides) - 1