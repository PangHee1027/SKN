def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i, number in enumerate(numbers) :
        while stack and numbers[stack[-1]] < number :
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))