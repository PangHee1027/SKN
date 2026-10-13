def facto(n) :
    result = 1
    for i in range(1, n + 1) :
        result *= i
    return result

def solution(n, k):
    answer = []
    digit = [i for i in range(1, n + 1)]
    remainder = k - 1
    n_facto = facto(n)
    for i in range(n, 0, -1) :
        n_facto //= i
        if i == 1 :
            answer.append(digit.pop())
            break
        quotient, remainder = divmod(remainder, n_facto)
        answer.append(digit.pop(quotient))
        if not remainder :
            answer += digit
            break
    return answer

print(solution(3, 5))