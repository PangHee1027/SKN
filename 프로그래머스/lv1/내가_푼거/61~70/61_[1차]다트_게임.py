def solution(dartResult):
    score = []
    stack = []
    for c in dartResult :
        if c == "S" :
            score.append(int("".join(stack)))
            stack = []
        elif c == "D" :
            score.append(int("".join(stack)) ** 2)
            stack = []
        elif c == "T" :
            score.append(int("".join(stack)) ** 3)
            stack = []
        elif c == "*" :
            score[-1] *= 2
            if len(score) != 1 :
                score[-2] *= 2
        elif c == "#" :
            score[-1] *= -1
        else :
            stack.append(c)
    answer = sum(score)
    return answer

print(solution("1S2D*3T"))