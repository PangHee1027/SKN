a, b, c = input().split()
b, c = int(b) + ((89 - int(a)) // 5) + 1, int(c)
result = ""

if (b > c) :
    result = "win"
elif (b < c) :
    result = "lose"
else :
    result = "same"

print(result)
