from itertools import combinations

def solution(line):
    meet = set()

    # 1. 모든 직선 쌍의 교점 구하기
    for (A1, B1, C1), (A2, B2, C2) in combinations(line, 2):
        denominator = A1 * B2 - B1 * A2
        
        # 평행하거나 일치하는 경우 (분모가 0)
        if denominator == 0:
            continue
            
        x_num = B1 * C2 - C1 * B2
        y_num = C1 * A2 - A1 * C2
        
        # 정수 좌표인 경우에만 추가
        if x_num % denominator == 0 and y_num % denominator == 0:
            x = x_num // denominator
            y = y_num // denominator
            meet.add((x, y))

    meet = list(meet)
    
    # 2. 모든 좌표를 양수로 평행이동하기 위한 보정값 계산
    min_x = min(p[0] for p in meet)
    min_y = min(p[1] for p in meet)
    
    # 격자판 크기 계산
    max_x = max(p[0] for p in meet)
    max_y = max(p[1] for p in meet)
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    # 3. 2차원 격자판 초기화 및 별 찍기
    board = [["." for _ in range(width)] for _ in range(height)]
    
    for x, y in meet:
        # 격자판 인덱스에 맞게 변환 (y축은 아래쪽이 0이므로 반전 적용)
        board[max_y - y][x - min_x] = "*"
        
    # 4. 문자열 리스트로 변환하여 반환
    return ["".join(row) for row in board]