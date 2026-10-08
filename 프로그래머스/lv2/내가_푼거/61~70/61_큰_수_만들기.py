def solution(number, k):
    remain = k
    while remain :
        cur = remain
        stack = []
        for n in number :
            while stack and stack[-1] < n and remain :
                stack.pop()
                remain -= 1
            stack.append(n)
        number = "".join(stack)
        if cur == remain :
            number = number[:-k]
            break

    return number

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))