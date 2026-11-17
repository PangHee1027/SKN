def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient :
        stack.append(i)
        while len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1] :
            answer += 1
            for _ in range(4) :
                stack.pop()

    return answer