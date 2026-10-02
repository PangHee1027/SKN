import heapq

def solution(scoville, K):
    # 1. O(N)으로 기존 리스트를 최소 힙으로 직접 변환
    heapq.heapify(scoville)
    count = 0

    # 2. 가장 작은 스코빌 지수가 K 미만일 때만 반복 진행
    while scoville[0] < K:
        # 더 이상 섞을 수 있는 음식이 남아있지 않은 경우
        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first + second * 2)
        count += 1

    return count