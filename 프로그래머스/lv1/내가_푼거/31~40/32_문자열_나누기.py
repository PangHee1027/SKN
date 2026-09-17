def solution(s):
    answer = 0
    target_char = ""
    target = 0
    other = 0
    
    for i, c in enumerate(s) :
        if target == 0 :
            target_char = c
        if c == target_char :
            target += 1
        else :
            other += 1
        if target == other :
            answer += 1
            target = 0
            other = 0
        else :
            if i == len(s) - 1 :
                answer += 1
    
    return answer

# print(solution("aaabbaccccabba"))