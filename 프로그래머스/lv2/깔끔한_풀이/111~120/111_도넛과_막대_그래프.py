from collections import defaultdict

def solution(edges):
    node = defaultdict(lambda : [0, 0])
    answer = [-1, 0, 0, 0]
    
    # 1. 모든 간선을 돌며 각 정점의 나가는 간선(out), 들어오는 간선(in) 기록
    for start, last in edges :
        node[start][0] += 1
        node[last][1] += 1

    # 2. 생성한 정점 찾기 (들어오는 간선이 0개이고, 나가는 간선이 2개 이상인 정점)
    for i, info in node.items() :
        out_line, in_line = info
        if in_line == 0 and out_line >= 2 :
            answer[0] = i
            total_graphs = out_line  # 총 그래프 수 (도넛 + 막대 + 8자)
            break
            
    # 3. 생성한 정점 제거 (이후 탐지 과정에서 혼선이 없도록 방지)
    node.pop(answer[0])

    # 4. 생성한 정점과 직접 연결되어 있던 노드들의 들어오는 간선 수 보정
    # (생성한 정점이 주었던 영향을 제거하기 위해 in_line을 1씩 감소)
    for start, end in edges :
        if start == answer[0] :
            node[end][1] -= 1

    # 5. 남은 정점들의 차수(Degree)를 확인하여 막대와 8자 그래프 개수 카운트
    for out_line, in_line in node.values() :
        if out_line == in_line == 2 :  # 8자 그래프의 중심 정점 특징
            answer[3] += 1
        elif out_line == 0 :            # 막대 그래프의 마지막 정점 특징
            answer[2] += 1

    # 6. 도넛 그래프 수 = (전체 그래프 수) - (막대 그래프 수) - (8자 그래프 수)
    answer[1] = total_graphs - answer[2] - answer[3]

    return answer