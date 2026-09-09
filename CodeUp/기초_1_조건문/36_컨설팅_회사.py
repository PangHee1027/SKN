a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
result = ""

if (a > b - c) :
    result = "do not advertise"
elif (a < b - c) :
    result = "advertise"
else :
    result = "does not matter"

print(result)
