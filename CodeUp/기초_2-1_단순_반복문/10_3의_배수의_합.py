a, b = input().split()
result = 0

for i in range(int(a), int(b) + 1) :
    result += i if i % 3 == 0 else 0 

print(result)
