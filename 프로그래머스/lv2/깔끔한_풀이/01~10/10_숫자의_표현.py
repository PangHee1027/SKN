def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 1:
                answer += 1
            if (n // i) != i and (n // i) % 2 == 1:  # 중복 세기 방지 및 정수 나눗셈
                answer += 1
    return answer