def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1) :
        if n % i == 0 :
            answer += 1 if i % 2 else 0
            if n / i > i :
                answer += 1 if (n / i) % 2 else 0
    return answer

print(solution(1))