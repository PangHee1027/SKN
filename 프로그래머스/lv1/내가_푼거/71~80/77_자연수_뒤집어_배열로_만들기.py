def solution(n):
    ls = []
    for i in range(len(str(n)) - 1, -1, -1) :
        ls.append(n // (10 ** i))
        n = n % (10 ** i)
    return ls[::-1]

print(solution(12345))