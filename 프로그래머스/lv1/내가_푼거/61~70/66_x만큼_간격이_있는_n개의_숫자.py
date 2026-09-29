def solution(x, n):
    # x = 0일때 런타임에러
    return [i for i in range(x, x * (n + 1), x)]
    
print(solution(-4, 2))