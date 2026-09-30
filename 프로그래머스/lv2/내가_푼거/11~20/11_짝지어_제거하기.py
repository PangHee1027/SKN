def solution(s):
    stack = []
    for c in s :
        stack.append(c)
        while len(stack) >= 2 and stack[-2] == stack[-1] :
            del(stack[-2:])
    return 0 if stack else 1

print(solution("cdcd"))