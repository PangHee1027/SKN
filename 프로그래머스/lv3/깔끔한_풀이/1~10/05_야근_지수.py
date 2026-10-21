import heapq

def solution(n, works):
    # 남은 일의 총합이 n보다 작거나 같으면 모든 일을 끝낼 수 있으므로 피로도는 0
    if sum(works) <= n:
        return 0

    # 최대 힙을 위해 부호 반전 후 heapify
    works = [-x for x in works]
    heapq.heapify(works)

    for _ in range(n):
        cur = heapq.heappop(works)
        cur += 1  # 음수이므로 +1을 하면 절댓값이 1 줄어듦 (작업량 1 감소)
        if cur:   # 작업량이 0이 아니라면 다시 힙에 푸시
            heapq.heappush(works, cur)

    # 남은 작업량들의 제곱의 합 계산
    return sum(work ** 2 for work in works)