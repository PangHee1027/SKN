from itertools import product

def solution(n, infection, edges, k):
    # 파이프 타입별로 간선 정보 저장 (튜플 활용)
    graph = {1: [], 2: [], 3: []}
    for node1, node2, p_type in edges:
        graph[p_type].append((node1, node2))
        graph[p_type].append((node2, node1))

    max_infection = 0

    # k번 파을 여는 모든 순서 탐색
    for order in product(range(1, 4), repeat=k):
        visited = {infection}
        
        for o in order:
            # 이번 파이프 타입(o)을 열었을 때 전파 시뮬레이션
            while True:
                added = False
                for u, v in graph[o]:
                    if u in visited and v not in visited:
                        visited.add(v)
                        added = True
                # 더 이상 새로 감염되는 배양체가 없다면 탈출
                if not added:
                    break
                    
        max_infection = max(max_infection, len(visited))

    return max_infection