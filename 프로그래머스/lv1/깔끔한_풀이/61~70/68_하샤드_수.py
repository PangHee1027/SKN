def solution(x):
    digit_sum = sum(int(c) for c in str(x))
    return x % digit_sum == 0