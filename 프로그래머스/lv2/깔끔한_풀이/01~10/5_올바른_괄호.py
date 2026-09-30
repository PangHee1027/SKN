def solution(s):
    if len(s) % 2 != 0 or s[0] == ")" or s[-1] == "(":
        return False

    count = 0
    for c in s:
        if count < 0:
            return False
        count += 1 if c == "(" else -1

    return count == 0