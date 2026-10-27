def solution(n, costs):
    # 1. 비용이 저렴한 다리부터 정렬
    costs.sort(key=lambda x: x[2])
    
    # 2. 부모 테이블 초기화 (자기 자신을 부모로 설정)
    parent = list(range(n))
    
    # find 함수 (경로 압축 적용)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # union 함수 (두 그룹 합치기)
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    cost = 0
    connected_edges = 0
    
    for i1, i2, c in costs:
        # 사이클이 생기지 않는 경우(서로 다른 그룹일 때)에만 연결
        if union(i1, i2):
            cost += c
            connected_edges += 1
            
            # 모든 섬이 연결되었다면(간선 개수 n-1개) 조기 종료
            if connected_edges == n - 1:
                break
                
    return cost