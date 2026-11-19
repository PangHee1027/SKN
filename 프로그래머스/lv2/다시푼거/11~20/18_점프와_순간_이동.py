def solution(n):
    answer = 0
    while n > 0 :
        n, mod = divmod(n, 2)
        answer += mod
        
    return answer