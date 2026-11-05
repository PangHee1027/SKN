from collections import Counter

def solution(a):
    n = len(a)
    if n == 1 :
        return 0
    
    count = sorted(dict(Counter(a)).items(), key =  lambda x : -x[1])
    answer = 0

    for key, c in count :
        if c * 2 < answer :
            continue
        stack = []
        for s in a :
            stack.append(s)
            if len(stack) % 2 :
                continue
            if stack[-1] == stack[-2] :
                stack.pop()
                continue
            if key not in (stack[-1], stack[-2]) :
                stack.pop()
        if len(stack) % 2 :
            stack.pop()
        if stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()
        if key not in (stack[-1], stack[-2]) :
            stack.pop()
            stack.pop()
        answer = max(len(stack), answer)

    return answer


print(solution([0,3,3,0,7,2,0,2,2,0]))