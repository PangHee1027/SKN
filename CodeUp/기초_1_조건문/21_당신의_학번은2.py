a, b, c = input().split()
b = b if (int(b) >= 10) else "0" + b
if (100 > int(c) >= 10) :
    c = "0" + c
elif (10 > int(c)) :
    c = "00" + c
print(a + b + c)
