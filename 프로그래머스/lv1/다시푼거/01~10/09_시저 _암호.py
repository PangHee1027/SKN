def solution(s, n):
    answer = ''
    
    for c in s :
        if c == ' ' :
            answer += c
            continue
        if ord('a') <= ord(c) <= ord('z') :
            i = (ord(c) - ord('a') + n) % 26
            answer += chr(ord('a') + i)
        else :
            i = (ord(c) - ord('A') + n) % 26
            answer += chr(ord('A') + i)
            
    return answer