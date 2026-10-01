def solution(s):
    # 1. 길이가 홀수이면 올바른 괄호 문자열이 불가능함
    if len(s) % 2 != 0:
        return 0

    pairs = {"]": "[", "}": "{", ")": "("}

    def is_correct(target):
        stack = []
        for c in target:
            if c in pairs:  # 닫는 괄호인 경우
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:  # 여는 괄호인 경우
                stack.append(c)
        return not stack

    answer = 0
    # 2. i만큼 회전한 문자열(s[i:] + s[:i])을 직접 전달
    for i in range(len(s)):
        if is_correct(s[i:] + s[:i]):
            answer += 1

    return answer