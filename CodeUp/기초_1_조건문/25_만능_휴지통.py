a = input()
b = []

for i in range(len(a)) :
    b.append(a[i - 1])

result = (int("".join(b)) * 2) % 100
print(result)
print("GOOD" if result <= 50 else "OH MY GOD")
