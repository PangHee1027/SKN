from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def solution(info, edges):
    def dfs(sheep, wolf, next_nodes) :
        result = []
        if not next_nodes :
            return sheep
        if wolf >= sheep :
            return sheep
        for node in next_nodes :
            next_nodes2 = next_nodes + graph[node]
            next_nodes2.remove(node)
            if info[node] :
                result.append(dfs(sheep, wolf + 1, next_nodes2))
            else :
                result.append(dfs(sheep + 1, wolf, next_nodes2))
            
        return max(result)

    graph = defaultdict(list)

    for parent, child in edges :
        graph[parent] += [child]

    return dfs(1, 0, graph[0])

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])) # 5
# print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])) # 5