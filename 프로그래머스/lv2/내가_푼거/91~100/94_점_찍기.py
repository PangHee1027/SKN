def solution(k, d):
    possible = 0
    sqrt_d = d ** 2

    for x in range (0, d + 1, k) :
        y = int((sqrt_d - x ** 2) ** 0.5)
        possible += y // k + 1

    return possible

print(solution(2, 4)) # 6
print(solution(1, 5)) # 26