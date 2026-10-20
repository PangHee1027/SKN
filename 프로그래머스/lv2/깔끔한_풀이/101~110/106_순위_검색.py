from bisect import bisect_left
from itertools import product
from collections import defaultdict

def solution(info, query):
    participant = defaultdict(list)
    
    # 1. 지원자 정보 전처리
    for record in info:
        words = record.split()
        scores = int(words[4])
        # 각 항목별로 (해당 값, "-") 중 하나를 고를 수 있도록 구성
        conditions = [(w, "-") for w in words[:4]]
        
        for c0, c1, c2, c3 in product(*conditions):
            participant[(c0, c1, c2, c3)].append(scores)

    # 2. 이진 탐색을 위해 각 조건별 점수 리스트 미리 정렬
    for key in participant:
        participant[key].sort()

    answer = []
    
    # 3. 쿼리 처리
    for q in query:
        q_words = q.replace("and", "").split()
        score_limit = int(q_words[4])
        
        satisfy = participant.get(tuple(q_words[:4]), [])
        # bisect_left를 이용해 기준 점수 이상인 사람들의 수 계산
        result = len(satisfy) - bisect_left(satisfy, score_limit)
        answer.append(result)

    return answer