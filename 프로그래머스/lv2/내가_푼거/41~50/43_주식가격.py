# 어케한거임? 나 스스로도 이해가 안되는데

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, p in enumerate(prices) :
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    for i in range(len(prices)) :
        while stack :
            idx = stack.pop()
            answer[idx] = len(prices) - idx - 1

    return answer

print(solution([1, 5, 4, 2, 3]))