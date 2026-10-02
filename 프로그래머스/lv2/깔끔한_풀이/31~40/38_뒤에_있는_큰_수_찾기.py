def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 인덱스를 저장할 스택

    for i in range(len(numbers)):
        # 스택이 비어있지 않고, 스택 top의 숫자보다 현재 숫자가 더 크면
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]  # 뒷 큰수 확정
            
        # 현재 인덱스를 스택에 추가
        stack.append(i)

    return answer