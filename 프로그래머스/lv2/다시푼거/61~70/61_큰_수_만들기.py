def solution(number, k):
    stack = []
    number = list(number)
    if len(number) - k == 1 :
        return str(max(number))
    
    for i, n in enumerate(number) :
        while k > 0 and stack and stack[-1] < n :
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0 :
        stack = stack[:-k]
        
    return ''.join(stack)