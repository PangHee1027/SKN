input()
b = input().split()

for i in range(len(b)) :
    b[i] = int(b[i])

print(max(b))
