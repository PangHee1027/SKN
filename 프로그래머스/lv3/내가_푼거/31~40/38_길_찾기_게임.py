import sys
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    node_idx = {tuple(node) : i + 1 for i, node in enumerate(nodeinfo)}
    nodeinfo = [tuple(node) for node in nodeinfo]
    nodeinfo.sort(key = lambda x : (x[1], -x[0]), reverse = True)
    graph = {}
    root = 0

    def preorder(node) :
        if not node :
            return []
        result = [node]

        left, right = graph[node].values()
        result += preorder(left)
        result += preorder(right)

        return result
    def postorder(node) :
        if not node :
            return []
        result = []

        left, right = graph[node].values()
        result += postorder(left)
        result += postorder(right)
        result += [node]

        return result
    
    for node in nodeinfo :
        graph[node] = {'left' : None, 'right' : None}
        if not root :
            root = node
            continue
        target = root
        while target :
            target_x = target[0]
            if node[0] < target_x :
                if graph[target]['left'] :
                    target = graph[target]['left']
                else :
                    graph[target]['left'] = node
                    break
            else :
                if graph[target]['right'] :
                    target = graph[target]['right']
                else :
                    graph[target]['right'] = node
                    break

    return [[node_idx[x] for x in preorder(root)], [node_idx[x] for x in postorder(root)]]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))