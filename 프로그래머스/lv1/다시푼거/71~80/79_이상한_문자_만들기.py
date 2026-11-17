def solution(s):
    answer = ''
    
    idx = 0
    for c in s :
        if c == ' ' :
            idx = 0
        else :
            idx += 1
        answer += c.upper() if idx % 2 else c.lower()
        
    return answer