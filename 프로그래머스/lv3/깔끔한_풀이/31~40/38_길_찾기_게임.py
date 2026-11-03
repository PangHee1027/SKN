import sys

# 트리의 최대 깊이가 1000 이하이므로 재귀 깊이 여유 설정
sys.setrecursionlimit(2000)


def solution(nodeinfo):
    # 1. 노드 번호 매핑 및 정렬 (y 내림차순, x 오름차순)
    node_idx = {tuple(node): i + 1 for i, node in enumerate(nodeinfo)}
    nodeinfo = sorted(nodeinfo, key=lambda x: (x[1], -x[0]), reverse=True)

    root = None
    graph = {tuple(node): {"left": None, "right": None} for node in nodeinfo}

    # 2. 이진 탐색 트리 구성
    for node in nodeinfo:
        node = tuple(node)
        if root is None:
            root = node
            continue

        target = root
        while True:
            if node[0] < target[0]:
                if graph[target]["left"] is None:
                    graph[target]["left"] = node
                    break
                target = graph[target]["left"]
            else:
                if graph[target]["right"] is None:
                    graph[target]["right"] = node
                    break
                target = graph[target]["right"]

    # 3. 전위 순회 (Preorder)
    def preorder(node, result):
        if node is None:
            return
        result.append(node_idx[node])
        preorder(graph[node]["left"], result)
        preorder(graph[node]["right"], result)

    # 4. 후위 순회 (Postorder)
    def postorder(node, result):
        if node is None:
            return
        postorder(graph[node]["left"], result)
        postorder(graph[node]["right"], result)
        result.append(node_idx[node])

    pre_res = []
    post_res = []

    preorder(root, pre_res)
    postorder(root, post_res)

    return [pre_res, post_res]