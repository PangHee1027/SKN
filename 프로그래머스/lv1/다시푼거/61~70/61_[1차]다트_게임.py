def solution(dartResult):
    stack = []
    scores = []
    for s in dartResult :
        if not stack and s.isdecimal():
            stack.append(s)
            continue
        if s == '#' :
            scores[-1] *= -1
        elif s == '*' :
            scores[-1] *= 2
            if len(scores) >= 2 :
                scores[-2] *= 2
        elif s in ('S', 'D', 'T') :
            score = int(''.join(stack))
            stack = []
            if s == 'S' :
                scores.append(score)
            elif s == 'D' :
                scores.append(score ** 2)
            else :
                scores.append(score ** 3)
        else :
            stack.append(s)
            
    return sum(scores)