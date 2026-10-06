import string

def solution(msg):
    lzw = list(string.ascii_uppercase)
    stack = []
    answer = []
    for i, s in enumerate(msg) :
        stack.append(s)
        if i < len(msg) - 1 :
            stack.append(msg[i + 1])
        stacked = "".join(stack)
        if i == len(msg) - 1 :
            answer.append(lzw.index(stacked) + 1)
            break
        if stacked not in lzw :
            lzw.append(stacked)
            answer.append(lzw.index("".join(stack[:-1])) + 1)
            if i < len(msg) - 1 :
                stack = []
        else :
            stack.pop()

    return answer

print(solution('ABABABABABABABAB'))
