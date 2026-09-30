def solution(n):
    # 1. 각 행의 크기에 맞게 2차원 배열 초기화
    triangle = [[0] * i for i in range(1, n + 1)]
    
    # 방향 정의: 아래, 오른쪽, 대각선 위 (행, 열)
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    row, col = 0, 0
    direction = 0  # 0: 아래, 1: 오른쪽, 2: 대각선 위
    
    # 2. 총 칸 수만큼 1부터 순서대로 채우기
    max_num = n * (n + 1) // 2
    for num in range(1, max_num + 1):
        triangle[row][col] = num
        
        # 다음 위치 계산
        next_row = row + dr[direction]
        next_col = col + dc[direction]
        
        # 범위를 벗어나거나 이미 값이 채워져 있다면 방향 전환
        if (next_row < 0 or next_row >= n or 
            next_col < 0 or next_col > next_row or 
            triangle[next_row][next_col] != 0):
            direction = (direction + 1) % 3
            next_row = row + dr[direction]
            next_col = col + dc[direction]
            
        row, col = next_row, next_col

    # 3. 2차원 배열을 1차원 리스트로 펼쳐서 반환
    return [val for row_list in triangle for val in row_list]

print(solution(4))  # [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]