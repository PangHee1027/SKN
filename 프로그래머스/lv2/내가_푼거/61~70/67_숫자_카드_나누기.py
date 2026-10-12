def get_gcd(num1, num2) :
    a, b = max(num1, num2), min(num1, num2)

    while b > 0 :
        a, b = b, a % b

    return a

def solution(arrayA, arrayB) :
    a = arrayA[0]
    for i in range(1, len(arrayA)) :
        a = get_gcd(a, arrayA[i])

    b = arrayB[0]
    for i in range(1, len(arrayB)) :
        b = get_gcd(b, arrayB[i])

    if a == 1 and b == 1 :
        return 0

    for num in arrayA :
        if not num % b :
            b = 0
            break

    for num in arrayB :
        if not num % a :
            a = 0
            break
    
    answer = 0
    return max(a, b)

print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))
