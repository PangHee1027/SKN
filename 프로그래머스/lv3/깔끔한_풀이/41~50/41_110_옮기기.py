def solution(s):
    answer = []
    for string in s:
        stack = []
        count = 0
        
        # 1. 스택을 이용해 '110'을 미리 추출하고 개수 세기 (슬라이싱 연산 최적화)
        for n in string:
            stack.append(n)
            while len(stack) >= 3 and stack[-1] == '0' and stack[-2] == '1' and stack[-3] == '1':
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1
                
        # 2. 스택에서 마지막 '0'의 위치 찾기
        idx = -1
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '0':
                idx = i
                break
                
        # 3. 결과 조합
        if idx == -1:
            answer.append('110' * count + "".join(stack))
        else:
            ans_str = "".join(stack[:idx + 1]) + ('110' * count) + "".join(stack[idx + 1:])
            answer.append(ans_str)
            
    return answer