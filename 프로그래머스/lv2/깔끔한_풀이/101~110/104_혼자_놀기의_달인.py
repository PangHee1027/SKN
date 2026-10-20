def solution(cards):
    visited = [False] * len(cards)
    groups = []

    for i in range(len(cards)):
        # 이미 다른 그룹에서 열어본 상자라면 스킵
        if visited[i]:
            continue
        
        # 새로운 그룹(사이클) 탐색 시작
        current_group = set()
        curr = i
        
        while not visited[curr]:
            visited[curr] = True
            current_group.add(cards[curr])
            curr = cards[curr] - 1  # 다음 열어야 할 상자의 인덱스
            
        groups.append(current_group)

    # 그룹의 개수가 1개 이하면 점수는 0점
    if len(groups) <= 1:
        return 0

    # 그룹 크기순으로 정렬 후 가장 큰 두 그룹의 크기 곱 반환
    groups.sort(key=len)
    return len(groups[-1]) * len(groups[-2])