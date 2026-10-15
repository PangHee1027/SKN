from itertools import combinations

def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])
    
    # 1개부터 컬럼 개수까지의 모든 조합 생성
    all_combinations = []
    for i in range(1, col_count + 1):
        all_combinations.extend(combinations(range(col_count), i))
        
    candidate_keys = []
    
    for comb in all_combinations:
        # 1. 최소성 검사: 이미 등록된 후보키가 현재 조합에 포함되어 있는지 확인
        is_minimal = True
        for key in candidate_keys:
            if key.issubset(comb):
                is_minimal = False
                break
        if not is_minimal:
            continue
            
        # 2. 유일성 검사: 해당 컬럼들의 조합으로 튜플을 유일하게 식별할 수 있는지 확인
        tuples = {tuple(row[idx] for idx in comb) for row in relation}
        
        if len(tuples) == row_count:
            candidate_keys.append(set(comb))
            
    return len(candidate_keys)