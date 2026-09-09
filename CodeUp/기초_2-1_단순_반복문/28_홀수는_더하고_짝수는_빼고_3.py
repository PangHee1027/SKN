a, b = input().split()
a, b = int(a), int(b)
result1 = 0
result2 = ""

while (a <= b) :
    if result1 == 0 :
        result2 += str(a) if a % 2 == 1 else str(-a)
    else :
        result2 += "+" + str(a) if a % 2 == 1 else str(-a)
    result1 += a if a % 2 == 1 else -a
    a += 1

print(result2 + "=" + str(result1))
    