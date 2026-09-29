def solution(x):
    x1 = str(x)
    sum = 0
    for c in x1 :
        sum += int(c)
    return x % sum == 0

print(solution(10))