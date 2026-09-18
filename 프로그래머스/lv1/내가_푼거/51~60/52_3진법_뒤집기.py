def solution(n):
    if n == 0:
        return 0
    else:
        result = ""
        while n > 0:
            result = str(n % 3) + result
            n //= 3
        answer = 0
        print(result)
        for i in range(len(result)) :
            answer += int(result[i]) * (3 ** i)
        return answer

# print(solution(45))