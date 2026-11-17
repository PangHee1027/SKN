def solution(absolutes, signs):
    return sum(x if s else -x for s, x in zip(signs, absolutes))