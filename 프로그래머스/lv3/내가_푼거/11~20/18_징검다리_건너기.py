from collections import deque

def solution(stones, k):
    n = len(stones)
    if n <= k:
        return max(stones)
    
    dq = deque()
    ans = float('inf')
    
    for i in range(n):
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        while dq and stones[dq[-1]] <= stones[i]:
            dq.pop()
            
        dq.append(i)
        
        if i >= k - 1:
            ans = min(ans, stones[dq[0]])
            
    return ans

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))