def solution(absolutes, signs):
    return sum(num if sign else -num for num, sign in zip(absolutes, signs))