# 두 수를 바꾸는 건 생각 못했던 거 같음
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
