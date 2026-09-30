def solution(arr):
    stack = []
    for i in arr:
        if stack[-1:] != [i]:
            stack.append(i)
    return stack