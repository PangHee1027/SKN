import sys

sys.setrecursionlimit(1000000)

def solution(n, computers):
    graph = {i : [] for i in range(n)}
    networks = set()

    for i, computer in enumerate(computers) :
        for j, c in enumerate(computer) :
            if c :
                graph[i].append(j)

    def dfs(i, visited) :
        visited.add(i)
        for computer in graph[i] :
            if computer not in visited :
                visited.update(dfs(computer, visited))
        return visited
    
    for i in graph.keys() :
        networks.add(tuple(dfs(i, set())))

    return len(networks)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))