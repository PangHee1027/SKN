def solution(sizes):
    heights = []
    width = []
    for i in sizes :
        heights.append(max(i))
        width.append(min(i))
    h = max(heights)
    w = max(width)
    answer = h * w
    return answer

# print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))