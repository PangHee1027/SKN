a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
result = ""

if (a * d > c * b) :
    result = ">"
elif (a * d < c * b) :
    result = "<"
else :
    result = "="

print(result)
