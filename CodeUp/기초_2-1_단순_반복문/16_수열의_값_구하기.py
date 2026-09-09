input = input().split()
a, b, c, n = int(input[0]), int(input[1]), int(input[2]), int(input[3])

for i in range(n - 1) :
    a = a * b + c

print(a)
