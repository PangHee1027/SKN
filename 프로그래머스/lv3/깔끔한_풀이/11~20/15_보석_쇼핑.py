def solution(gems):
    n = len(gems)
    total_kinds = len(set(gems))  # 전체 보석의 종류 수
    
    gem_dict = {}
    left = 0
    result = [0, n]  # [시작, 끝] 번호 초기화
    
    for right in range(n):
        gem = gems[right]
        # 딕셔너리에 보석 추가 (없으면 0에서 시작)
        gem_dict[gem] = gem_dict.get(gem, 0) + 1
        
        # 윈도우 안에 모든 종류의 보석이 다 들어왔다면, left를 당기며 최단 구간 탐색
        while len(gem_dict) == total_kinds:
            # 현재 구간이 기존 최단 구간보다 짧다면 갱신
            if right - left < result[1] - result[0]:
                result = [left + 1, right + 1]  # 1부터 시작하는 번호로 변환
            
            # 왼쪽 보석을 빼기 전 처리
            left_gem = gems[left]
            gem_dict[left_gem] -= 1
            
            # 개수가 0이 되면 딕셔너리에서 완전히 제거 (종류 수도 1 감소 효과)
            if gem_dict[left_gem] == 0:
                del gem_dict[left_gem]
            
            left += 1
            
    return result