from collections import defaultdict

def solution(edges):
    node = defaultdict(lambda : [0, 0])
    answer = [-1, 0, 0, 0]
    num_of_graph = 0

    for start, last in edges :
        node[start][0] += 1
        node[last][1] += 1

    for i, info in node.items() :
        out_line, in_line = info
        if in_line == 0 and out_line >= 2 :
            answer[0] = i
            num_of_graph = out_line
            break
    node.pop(answer[0])

    for start, end in edges :
        if start != answer[0] :
            continue
        node[end][1] -= 1

    for out_line, in_line in node.values() :
        if out_line == in_line == 2 :
            answer[3] += 1
        elif out_line == 0 :
            answer[2] += 1

    answer[1] = num_of_graph - answer[2] - answer[3]

    return answer

print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))