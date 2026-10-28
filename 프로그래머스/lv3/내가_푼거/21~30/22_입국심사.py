def solution(n, times):
    left, right = 1, n * max(times)
    while left < right :
        mid = (left + right) // 2
        capacity = 0
        for time in times :
            capacity += mid // time
        if capacity < n :
            left = mid + 1
        else :
            right = mid
    return left

print(solution(6, [7, 10]))