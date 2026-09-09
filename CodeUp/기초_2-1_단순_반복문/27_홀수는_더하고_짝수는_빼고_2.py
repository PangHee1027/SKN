a, b = input().split()
a, b = int(a), int(b)
result1 = 0
result2 = ""

while (a <= b) :
    result1 += a if a % 2 == 1 else -a
    result2 += "+" + str(a) if a % 2 == 1 else str(-a)
    a += 1

print(result2 + "=" + str(result1))
    