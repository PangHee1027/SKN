import heapq

def solution(k, score):
    fame = []  # 명예의 전당 (최소 힙)
    answer = []

    for s in score:
        heapq.heappush(fame, s)
        
        # 명예의 전당 인원이 k명을 초과하면 가장 낮은 점수 제거
        if len(fame) > k:
            heapq.heappop(fame)
            
        # 힙의 0번 인덱스는 항상 최하위 점수
        answer.append(fame[0])

    return answer