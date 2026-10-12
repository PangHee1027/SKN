import heapq

def solution(n, k, enemy):
    heap = []
    
    for i, num in enumerate(enemy):
        heapq.heappush(heap, num)
        # 만약 진행한 라운드 수가 무적권(k)보다 많다면, 
        # 가장 적의 수가 적었던 라운드는 무적권을 빼고 병사로 막아야 합니다.
        if len(heap) > k:
            n -= heapq.heappop(heap)
            
        # 병사가 부족해지면 더 이상 진행 불가 (현재까지의 인덱스가 버틴 라운드 수)
        if n < 0:
            return i
            
    # 에러 없이 끝까지 다 돌았다면 모든 라운드 클리어
    return len(enemy)