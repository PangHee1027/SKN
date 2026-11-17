def solution(s):
    count = 0
    for c in s :
        if count < 0 :
            return False
        count += 1 if c == "(" else -1
    return count == 0

print(solution(")()("))