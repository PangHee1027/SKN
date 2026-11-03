from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def solution(info, edges):
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
        
    max_sheep = 0

    def dfs(sheep, wolf, next_nodes):
        nonlocal max_sheep
        # 현재까지 모은 양의 수로 최댓값 갱신
        max_sheep = max(max_sheep, sheep)
        
        for node in next_nodes:
            next_sheep, next_wolf = sheep, wolf
            
            if info[node] == 1:
                next_wolf += 1
            else:
                next_sheep += 1
                
            # 늑대가 양을 잡아먹는 경우 가지치기
            if next_wolf >= next_sheep:
                continue
                
            # 다음 방문 가능한 후보군 갱신 (set 활용)
            next_nodes2 = (next_nodes - {node}) | set(graph[node])
            dfs(next_sheep, next_wolf, next_nodes2)

    # 루트 노드(0)에서 시작 (루트의 자식들을 초기 후보군으로 설정)
    dfs(1, 0, set(graph[0]))
    
    return max_sheep