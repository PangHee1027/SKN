def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 0
    last_end = -float("inf")

    for s, e in routes :
        if s > last_end:
            answer += 1
            last_end = e

    return answer

print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))