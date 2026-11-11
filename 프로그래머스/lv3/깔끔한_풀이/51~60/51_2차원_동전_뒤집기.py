def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    min_count = float('inf')

    # 행을 뒤집는 모든 경우의 수를 비트마스크로 탐색 (0부터 2^n - 1)
    for i in range(1 << n):
        count = 0
        board = [row[:] for row in beginning]
        
        # 비트가 1인 행은 미리 뒤집기
        for r in range(n):
            if (i >> r) & 1:
                count += 1
                for c in range(m):
                    board[r][c] = 1 - board[r][c]
        
        # 각 열을 확인하여 target과 다르면 열 뒤집기 수행
        possible = True
        for c in range(m):
            # 첫 번째 행과 비교하여 이 열이 뒤집혀야 하는지 판단
            diff = board[0][c] != target[0][c]
            for r in range(n):
                current = board[r][c] if not diff else 1 - board[r][c]
                if current != target[r][c]:
                    possible = False
                    break
            if not possible:
                break
            if diff:
                count += 1
                
        if possible:
            min_count = min(min_count, count)

    return min_count if min_count != float('inf') else -1