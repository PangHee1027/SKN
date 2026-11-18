def solution(string):
    answer = ''
    idx = 0
    for s in string :
        if s == ' ' :
            idx = 0
        else :
            idx += 1
        if idx == 1 :
            answer += s.upper()
        else :
            answer += s.lower()
    return answer