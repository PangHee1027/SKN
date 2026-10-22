def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 0
    return routes

print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))