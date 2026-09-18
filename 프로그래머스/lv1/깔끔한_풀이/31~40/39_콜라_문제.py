def solution(a, b, n):
    answer = 0
    while n >= a:
        new_coke, remainder = divmod(n, a)
        answer += new_coke * b
        n = new_coke * b + remainder
    return answer