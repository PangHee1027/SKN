def solution(s):
    min_len = len(s)
    max_compression = min_len // 2

    for i in range(1, max_compression + 1) :
        cur_s = [s[x : x + i] for x in range(0, len(s), i)]
        stack = []
        cur_len = 0

        for string in cur_s :
            if not stack :
                stack.append(string)
                continue
            if string == stack[-1] :
                stack.append(string)
            else :
                cur_len += len(stack[-1])
                cur_len += len(str(len(stack))) if len(stack) > 1 else 0
                stack = [string]
        cur_len += len(stack[-1])
        cur_len += len(str(len(stack))) if len(stack) > 1 else 0
        min_len = min(min_len, cur_len)

    return min_len

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17
