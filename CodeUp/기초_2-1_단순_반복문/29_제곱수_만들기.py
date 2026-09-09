a = int(input())
b = 0

while True :
    if a ** 0.5 % 1 == 0 :
        a = int(a ** 0.5)
        break
    else :
        a -= 1
        b += 1

print(b, a) 
