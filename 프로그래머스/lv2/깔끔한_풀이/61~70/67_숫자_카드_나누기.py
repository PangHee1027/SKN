def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_array_gcd(arr):
    gcd_val = arr[0]
    for num in arr[1:]:
        gcd_val = get_gcd(gcd_val, num)
    return gcd_val

def solution(arrayA, arrayB):
    # 1. 각 배열의 전체 최대공약수(GCD) 구하기
    a = get_array_gcd(arrayA)
    b = get_array_gcd(arrayB)

    # 2. 조건 검증: A의 GCD(a)가 B의 원소를 하나라도 나눌 수 있다면 a는 무효화(0)
    for num in arrayB:
        if num % a == 0:
            a = 0
            break

    # 3. 조건 검증: B의 GCD(b)가 A의 원소를 하나라도 나눌 수 있다면 b는 무효화(0)
    for num in arrayA:
        if num % b == 0:
            b = 0
            break
    
    return max(a, b)