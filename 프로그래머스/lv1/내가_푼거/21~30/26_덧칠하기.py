def solution(n, m, section):
    wall = [1] * n
    answer = 0
    for i in section :
        wall[i - 1] = 0

    for i in range(len(wall)) :
        if wall[i] == 0 :
            for j in range(i, min(i + m, len(wall))) :
                wall[j] = 1
            answer += 1
    
    return answer

# print(solution(5, 4, [1, 3]))