input()
b = input().split()
result = 0

for i in b :
    result += int(i) if int(i) % 5 == 0 else 0

print(result)
