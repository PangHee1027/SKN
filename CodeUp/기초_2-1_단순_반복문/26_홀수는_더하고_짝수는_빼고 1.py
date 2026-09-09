a, b = input().split()
a, b = int(a), int(b)
result = 0

while (a <= b) :
    result += a if a % 2 == 1 else -a
    a += 1

print(result)
    