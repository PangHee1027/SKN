input()
b = input().split()
result = 0

for i in b :
    result += 1 if int(i) % 2 == 1 else 0

print(result)
