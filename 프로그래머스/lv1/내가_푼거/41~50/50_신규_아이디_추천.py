def solution(new_id):
    special_char = "~!@#$%^&*()=+[{]}:?,<>/"
    new_id = new_id.lower()
    for sc in special_char :
        new_id = new_id.replace(sc, "")
    stack = []
    for i in new_id :
        stack.append(i)
        if len(stack) == 1 :
            continue
        if stack[-2:] == [".", "."] :
            del stack[-1]
    if len(stack) > 0 and stack[0] == "." :
        del stack[0]
    if len(stack) > 0 and stack[-1] == "." :
        del stack[-1]
    if len(stack) == 0 :
        stack += ["a"]
    stack = stack[:15]
    if stack[-1] == "." :
        del stack[-1]
    while len(stack) < 3 :
        stack += stack[-1:]
    new_id = "".join(stack)

    return new_id

# print(solution("abcdefghijklmn.p"))