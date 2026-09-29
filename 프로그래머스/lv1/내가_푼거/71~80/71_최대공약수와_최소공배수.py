def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1) :
        if n % i == 0 and m % i == 0 :
            answer.append(i)
            break
    else :
        answer.append(1)
    for i in range(max(n, m), n * m + 1, max(n, m)) :
        if i % n == 0 and i % m == 0 :
            answer.append(i)
            break
    else :
        answer.append(n * m)
    return answer

print(solution(11, 22))