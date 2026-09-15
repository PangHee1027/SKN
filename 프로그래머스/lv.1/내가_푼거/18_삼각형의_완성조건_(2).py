def solution(sides):
    answer = 0

    for i in range(0, max(sides) + 1) :
        if min(sides) + i > max(sides) :
            answer += 1
    for i in range(sum(sides), max(sides), - 1) :
        if i < sum(sides) :
            answer += 1
    return answer

# print(solution([11, 7]))