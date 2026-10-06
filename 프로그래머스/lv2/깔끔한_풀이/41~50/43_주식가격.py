def solution(prices):
    length = len(prices)
    answer = [0] * length
    stack = []

    # 1. 주식 가격이 떨어지는 시점 처리
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
        
    # 2. 끝까지 가격이 떨어지지 않은 주식들 정리
    while stack:
        idx = stack.pop()
        answer[idx] = length - idx - 1
        
    return answer