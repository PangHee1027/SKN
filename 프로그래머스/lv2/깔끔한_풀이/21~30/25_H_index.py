def solution(citations):
    # 1. 내림차순 정렬
    citations.sort(reverse=True)
    
    # 2. 인용 횟수가 논문 수(i + 1)보다 작아지는 지점 탐색
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i
            
    # 모든 논문의 인용 횟수가 전체 논문 수 이상인 경우
    return len(citations)