def solution(stones, k):
    # 'mid'명이 건널 수 있는지 판별하는 함수
    def can_cross(mid):
        consecutive = 0
        for stone in stones:
            # mid명이 건넌 후에도 0 이하가 되면 밟을 수 없는 돌
            if stone - mid < 0:
                consecutive += 1
                if consecutive >= k:
                    return False  # 연속으로 k개 이상 못 건너면 실패
            else:
                consecutive = 0  # 밟을 수 있는 돌을 만나면 연속 카운트 초기화
        return True

    # 이분 탐색 범위 설정 (최소 1명 ~ 디딤돌 최대값)
    low = 1
    high = max(stones)
    answer = 1

    while low <= high:
        mid = (low + high) // 2
        
        if can_cross(mid):
            answer = mid       # 건널 수 있다면 인원을 더 늘려서 시도
            low = mid + 1
        else:
            high = mid - 1     # 못 건넌다면 인원을 줄여서 시도

    return answer