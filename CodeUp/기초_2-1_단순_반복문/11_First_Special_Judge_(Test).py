a = input().split()

for i in a :
    if int(i) % 5 == 0 :
        print(int(i))
        break
else :
    print(0)
