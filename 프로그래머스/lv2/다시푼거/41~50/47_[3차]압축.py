import string

def solution(msg):
    lzw = {x : i + 1 for i, x in enumerate(string.ascii_lowercase)}
    lzw_key = set(list(string.ascii_lowercase))
    nxt = 27
    result = []
    stack = ''
    msg = msg.lower()
    for s in msg :
        pre = stack
        stack += s
        if stack and stack in lzw_key :
            continue
        if stack not in lzw_key :
            result.append(lzw[pre])
            lzw[stack] = nxt
            lzw_key.add(stack)
            nxt += 1
            stack = s
            
    result.append(lzw[stack])
    return result