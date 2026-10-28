from collections import deque

def solution(n, edge):
    # 1. 1번 노드부터 n번 노드까지 최단 거리를 저장할 배열 (-1로 초기화)
    distance = [-1] * (n + 1)
    distance[1] = 0
    
    # 2. 딕셔너리 대신 더 빠르고 가벼운 2차원 리스트(배열)로 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)

    # 3. BFS 탐색 시작
    dq = deque([1])
    while dq:
        node = dq.popleft()
        require = distance[node] + 1
        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = require
                dq.append(next_node)

    # 4. max()와 count()를 따로 쓰지 않고, 배열을 한 번만 순회하며 최댓값과 개수 동시에 카운트
    max_dist = 0
    count = 0
    for d in distance[1:]:  # 1번 노드부터 n번 노드까지 확인
        if d > max_dist:
            max_dist = d
            count = 1
        elif d == max_dist:
            count += 1

    return count