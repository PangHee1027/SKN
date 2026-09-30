def solution(s):
    stack = []
    answer = ""
    length = 0
    for c in s :
        if c == " " :
            answer = answer + ("".join(stack) if len(stack) else "") + c
            stack = []
            length = 0
            continue
        stack.append(c.lower() if length % 2 else c.upper())
        length += 1

    return answer + ("".join(stack) if len(stack) else "")

print(solution("try hello world"))