def solution(n, wires) :
    def dfs(node, remove_wire, visited) :
        v1, v2 = remove_wire
        for nxt in graph[node] :
            if nxt in visited :
                continue
            if (node, nxt) == (v1, v2) :
                continue
            if (node, nxt) == (v2, v1) :
                continue
            visited.add(nxt)
            dfs(nxt, remove_wire, visited)
        return len(visited)
        
    graph = {i : [] for i in range(1, n + 1)}
    answer = n
    for v1, v2 in wires :
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for wire in wires :
        tower = dfs(1, wire, {1})
        answer = min(answer, abs(tower - (n - tower)))
    return answer