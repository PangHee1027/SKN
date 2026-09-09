n = int(input())
result = 0

for i in range(1, n + 1) :
    result += i if i % 2 == 0 else 0 

print(result)
