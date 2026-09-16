def hanoi (n, start, sub, last) :
    if n == 1 :
        return [[start, last]]
    return hanoi(n - 1, start, last, sub) + [[start, last]] + hanoi(n - 1, sub, start, last)

def solution(n):
    return hanoi(n, 1, 2, 3)

# print(solution(3))