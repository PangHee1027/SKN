a, b = input().split()

a = int(a) if int(b) >= 30 else (int(a) - 1 if a != "0" else 23)
b = int(b) - 30 if int(b) >= 30 else int(b) + 30
print(a, b)
