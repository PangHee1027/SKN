a = int(input())

if a == 0:
    print(0)
else:
    result = ""
    while a > 0:
        result = str(a % 2) + result
        a //= 2
    print(result)
