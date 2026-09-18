from itertools import combinations

def solution(numbers):
    answer = list(set(x + y for x, y in list(combinations(numbers, 2))))
    answer.sort()
    return answer

# print(solution([2,1,3,4,1]))