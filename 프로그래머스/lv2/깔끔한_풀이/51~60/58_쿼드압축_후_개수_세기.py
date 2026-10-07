def solution(arr):
    answer = [0, 0]  # [0의 개수, 1의 개수]

    def compress(x, y, n):
        first = arr[x][y]
        
        # 1. 현재 영역(n x n)의 모든 원소가 같은지 검사
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != first:
                    # 다르면 4개의 사분면으로 분할 재귀 호출
                    half = n // 2
                    compress(x, y, half)                  # 좌상
                    compress(x, y + half, half)           # 우상
                    compress(x + half, y, half)           # 좌하
                    compress(x + half, y + half, half)    # 우하
                    return

        # 2. 모두 같다면 해당 숫자 카운트 증가
        answer[first] += 1

    # (0, 0) 위치부터 전체 크기(len(arr))로 시작
    compress(0, 0, len(arr))
    return answer