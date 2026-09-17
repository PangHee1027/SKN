def solution(number, limit, power):
    # 1부터 number까지 각 숫자의 약수 개수를 저장할 배열
    divisors = [0] * (number + 1)

    # 각 i의 배수들에 약수 개수(+1)를 가산
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1

    # limit 초과 여부 확인 후 합산
    return sum(d if d <= limit else power for d in divisors[1:])