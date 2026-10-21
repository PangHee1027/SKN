from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(begin)

    def can_convert(w1, w2):
        # 한 글자만 다른지 확인하는 함수
        return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1

    # BFS 탐색 (큐에 현재 단어와 단계 수를 저장)
    dq = deque([(begin, 0)])
    visited = {begin}

    while dq:
        cur, count = dq.popleft()
        
        # target에 도달했다면 그 즉시 단계 수 반환 (BFS이므로 최단 거리 보장)
        if cur == target:
            return count

        # words 중에서 아직 방문하지 않았고, 한 글자만 바꿀 수 있는 단어 탐색
        for nxt in words:
            if nxt not in visited and can_convert(cur, nxt):
                visited.add(nxt)
                dq.append((nxt, count + 1))

    return 0