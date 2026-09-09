a = int(input())
count = 0

while True :
    if (a // 10 != 0) :
        count += 1
        a = a // 10
    else :
        count += 1
        break

print(count)
