def solution(s):
    answer = ""
    is_first = True
    for c in s :
        if c == " " :
            is_first = True
            answer += c
        else :
            if is_first :
                answer += c.upper()
                is_first = False
            else :
                answer += c.lower()    
    return answer

print(solution("3people unFollowed me"))