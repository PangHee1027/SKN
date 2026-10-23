def solution(n, stations, w):
    answer = 0
    cover = 1 + 2 * w
    start = 1  # 현재 탐색 중인 아파트 위치

    for station in stations:
        left_bound = station - w  # 현재 기지국이 커버하는 시작점
        
        # 기지국 전까지 빈 구간이 존재한다면
        if start < left_bound:
            necessary = left_bound - start
            answer += (necessary + cover - 1) // cover
            
        # 다음 탐색 시작점을 현재 기지국이 커버하는 구간 바로 다음으로 갱신
        start = station + w + 1

    # 마지막 기지국 이후에 남은 빈 구간 처리
    if start <= n:
        necessary = n - start + 1
        answer += (necessary + cover - 1) // cover

    return answer