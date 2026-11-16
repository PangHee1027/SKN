def solution(n, m, x, y, queries):
    min_row, max_row, min_col, max_col = x, x, y, y
    
    # 역추적을 위해 쿼리 순서를 거꾸로 뒤집습니다.
    for mode, dist in reversed(queries):
        if mode == 0:
            # 원래: 왼쪽 이동 (열 감소) -> 역추적: 오른쪽으로 확장
            max_col = min(m - 1, max_col + dist)
            if min_col != 0:
                min_col = max(0, min_col + dist)
            if max_col < 0:
                return 0
                
        elif mode == 1:
            # 원래: 오른쪽 이동 (열 증가) -> 역추적: 왼쪽으로 확장
            min_col = max(0, min_col - dist)
            if max_col != m - 1:
                max_col = min(m - 1, max_col - dist)
            if min_col >= m:
                return 0
                
        elif mode == 2:
            # 원래: 위쪽 이동 (행 감소) -> 역추적: 아래쪽으로 확장
            max_row = min(n - 1, max_row + dist)
            if min_row != 0:
                min_row = max(0, min_row + dist)
            if max_row < 0:
                return 0
                
        elif mode == 3:
            # 원래: 아래쪽 이동 (행 증가) -> 역추적: 위쪽으로 확장
            min_row = max(0, min_row - dist)
            if max_row != n - 1:
                max_row = min(n - 1, max_row - dist)
            if min_row >= n:
                return 0

    return (max_col - min_col + 1) * (max_row - min_row + 1)