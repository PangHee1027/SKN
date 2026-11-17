def solution(s):
    answer = 0
    target = ''
    count = 0
    for c in s :
        if not target :
            target = c
            count = 1
            continue
        if c == target :
            count += 1
        else :
            count -= 1
        if not count :
            target = ''
            count = 1
            answer += 1
    if target :
        answer += 1
    return answer