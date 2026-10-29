def solution(scores):
    # 1. 원래 인덱스를 함께 저장 (완호 = 인덱스 0)
    indexed_scores = [(score[0], score[1], i) for i, score in enumerate(scores)]
    
    # 2. 근무 태도 점수 내림차순, 동료 평가 점수 오름차순 정렬
    indexed_scores.sort(key=lambda x: (-x[0], x[1]))
    
    survived = []
    limit_b = indexed_scores[0][1]
    wanho_sum = scores[0][0] + scores[0][1]
    
    for a, b, idx in indexed_scores:
        if b < limit_b:
            # 인덱스 0이 완호이므로 완호가 탈락한 경우 즉시 -1 반환
            if idx == 0:
                return -1
            continue
        else:
            survived.append(a + b)
            limit_b = b

    # 3. 완호보다 점수 합이 큰 사람의 수 + 1이 완호의 석차
    return sum(1 for total in survived if total > wanho_sum) + 1