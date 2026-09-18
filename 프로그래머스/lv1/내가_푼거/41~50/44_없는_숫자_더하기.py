def solution(numbers):
    s = set(range(10))
    answer = sum(s.difference(set(numbers)))
    return answer

# print(solution([5,8,4,0,6,7,9]))