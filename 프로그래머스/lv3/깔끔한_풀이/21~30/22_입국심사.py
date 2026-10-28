def solution(n, times):
    left, right = 1, n * max(times)
    while left < right:
        mid = (left + right) // 2
        
        # for문 대신 sum을 사용해 한 줄로 심사 가능 인원 계산
        capacity = sum(mid // time for time in times)
        
        if capacity < n:
            left = mid + 1
        else:
            right = mid
            
    return left