def solution(s):
    stack = []
    
    for c in s :
        stack.append(c)
        
        while len(stack) > 1 and stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()

    return 0 if stack else 1