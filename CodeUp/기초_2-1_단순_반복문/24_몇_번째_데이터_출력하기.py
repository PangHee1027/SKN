input()
b = input().split()
result = [int(b[0]), int(b[len(b) // 2]), int(b[len(b) - 1])]

for i in result :
    print(i, end = " ")
