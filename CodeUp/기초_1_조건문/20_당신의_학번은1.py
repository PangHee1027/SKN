a, b, c = input().split()
print(a + b + c if (int(c) >= 10) else a + b + "0" + c)
