from collections import deque

def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    dr = ((1, 0), (0, 1), (-1, -1))
    target = n * (n + 1) // 2
    dq = deque(range(1, target + 1))
    x, y = -1, 0
    for i in range(n) :
        for j in range(n - i) :
            dx, dy = dr[i % 3]
            x, y = x + dx, y + dy
            triangle[x][y] = dq.popleft()
    
    answer = []
    
    for row in triangle :
        answer += row
        
    return answer