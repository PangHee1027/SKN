def solution(n):
    answer = 0

    for i in range(2, n + 1) :
        for j in range (1, int(i ** 0.5) + 1) :
            if j != 1 and i % j == 0 :
                break
        else :
            answer += 1

    return answer

print(solution(10))