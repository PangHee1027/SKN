def solution(n) :
    digit = '124'
    answer = ''
    while n > 0 :
        n -= 1
        n, mod = divmod(n, 3)
        answer += digit[mod]
    return answer[::-1]