from itertools import combinations

def solution(n, q, ans):
    # 1. 처음부터 세트로 생성하여 리스트->세트 변환 비용 제거
    possible = set(combinations(range(1, n + 1), 5))

    for q_x, ans_x in zip(q, ans):
        q_set = set(q_x)  # 2. q_x는 쿼리당 한 번만 세트로 변환
        
        # 3. p는 튜플이므로 set(p) 없이 intersection에 바로 전달
        possible = {p for p in possible if len(q_set.intersection(p)) == ans_x}
            
    return len(possible)