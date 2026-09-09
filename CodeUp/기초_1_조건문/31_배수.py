a, b = input().split()
a, b = int(a), int(b)
result = ""

if (b % a == 0) :
    result = f"{a}*{b // a}={b}"
elif (a % b == 0) :
    result = f"{b}*{a // b}={a}"
else :
    result = "none"

print(result)
