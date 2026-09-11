a = input()
b = []

b = "".join([a[i] for i in range(len(a) - 1, -1, -1)])

secret = str(int(a) + int(b))
for i in range(len(secret) // 2) :
    if secret[i] != secret[len(secret) - 1 - i] :
        print("NO")
        break
else :
    print("YES")
