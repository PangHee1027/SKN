def solution(a, b, n):
    answer = 0
    while n >= a :
        remainder = 0
        answer += (n // a) * b
        remainder += n % a
        n = (n // a) * b + remainder
    return answer

# print(solution(3,1,20))