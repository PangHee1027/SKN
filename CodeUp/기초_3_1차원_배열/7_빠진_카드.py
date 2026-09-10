a = int(input())
b = []

for i in range(a - 1) :
    b.append(int(input()))

b.sort()

for i in range(len(b)) :
    if i + 1 != b[i] :
        print(i + 1)
        break
else :
    print(len(b) + 1)
