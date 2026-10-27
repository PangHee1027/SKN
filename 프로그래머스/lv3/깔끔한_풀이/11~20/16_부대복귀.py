from collections import deque

def solution(n, roads, sources, destination):
    # 1. 딕셔너리 대신 리스트의 리스트를 사용하여 속도 및 메모리 최적화
    graph = [[] for _ in range(n + 1)]
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    # 2. region 배열 자체가 방문 체크와 거리 저장을 동시에 담당 (-1이면 미방문)
    region = [-1] * (n + 1)
    region[destination] = 0

    dq = deque([destination])

    while dq:
        cur = dq.popleft()
        require = region[cur] + 1
        
        for nxt in graph[cur]:
            # region 값이 -1이라는 것은 아직 방문하지 않았다는 뜻
            if region[nxt] == -1:
                region[nxt] = require
                dq.append(nxt)

    return [region[i] for i in sources]