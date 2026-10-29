def solution(a):
    n = len(a)
    if n <= 2:
        return n
        
    # 1. 왼쪽에서부터의 최솟값을 기록하는 배열
    left_min = [0] * n
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])
        
    # 2. 오른쪽에서부터의 최솟값을 기록하는 배열
    right_min = [0] * n
    right_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
        
    possible = 0
    
    # 3. 각 풍선이 살아남을 수 있는지 판별
    for i in range(n):
        # 양 끝 풍선은 항상 살아남을 수 있음
        if i == 0 or i == n - 1:
            possible += 1
        # 현재 풍선이 왼쪽 최솟값 혹은 오른쪽 최솟값 중 하나보다 작다면 생존 가능
        elif a[i] < left_min[i - 1] or a[i] < right_min[i + 1]:
            possible += 1
            
    return possible