def solution(picks, minerals):
    # 곡괭이별 광물 채취 피로도 테이블
    fatigue_table = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }
    
    dia, iron, stone = picks
    
    # 5개씩 광물 묶음 생성 후, 가용한 곡괭이 개수만큼만 자르기
    chunks = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]
    
    # 각 묶음별로 [다이아 곡괭이 피로도, 철 곡괭이 피로도, 돌 곡괭이 피로도] 계산
    evaluated_chunks = []
    for chunk in chunks:
        cost = [0, 0, 0]
        for mine in chunk:
            for j in range(3):
                cost[j] += fatigue_table[mine][j]
        evaluated_chunks.append(cost)
        
    # 돌 곡괭이로 캘 때 피로도가 큰 순서(가장 어려운 묶음)대로 정렬
    evaluated_chunks.sort(key=lambda x: x[2], reverse=True)
    
    answer = 0
    for cost in evaluated_chunks:
        if dia > 0:
            answer += cost[0]
            dia -= 1
        elif iron > 0:
            answer += cost[1]
            iron -= 1
        else:
            answer += cost[2]
            stone -= 1
            
    return answer