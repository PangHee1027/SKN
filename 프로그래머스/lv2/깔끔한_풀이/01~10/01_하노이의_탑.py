def hanoi(n, start, end, via):
    if n == 1:
        return [[start, end]]
    return hanoi(n - 1, start, via, end) + [[start, end]] + hanoi(n - 1, via, end, start) 

def solution(n):
    return hanoi(n, 1, 3, 2)

# print(solution(3))