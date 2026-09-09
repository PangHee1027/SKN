a = int(input())
input()
b = input().split()
result = a * 1.0

for i in range(len(b)) :
    result = result * (100 + int(b[i])) * 0.01

print(format(result - a, "0.0f"))

if result > a :
    print("good")
elif result < a :
    print("bad")
else :
    print("same")
