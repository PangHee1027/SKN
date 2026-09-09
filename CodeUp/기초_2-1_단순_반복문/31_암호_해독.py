a = int(input())
num1, num2 = 0, 0

def is_prime(n) :
    count = 0
    for i in range(1, n + 1) :
        count += 1 if n % i == 0 else 0
    return True if count == 2 else False

for i in range(1, a + 1) :
    if is_prime(i) :
        if a % i == 0 :
            num1, num2 = i, a // i
            break

if is_prime(num2) :
    print(num1, num2)
else :
    print("wrong number")
