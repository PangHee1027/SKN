def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()  # 짝이 맞으면 기존 원소 제거
        else:
            stack.append(c)  # 짝이 안 맞으면 추가
            
    return 0 if stack else 1