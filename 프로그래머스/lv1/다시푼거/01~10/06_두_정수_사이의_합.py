def solution(a, b) :
    s, e = min(a, b), max(a, b)
    answer = 0
    for i in range(s, e + 1, 1) :
        answer += i
    
    return answer