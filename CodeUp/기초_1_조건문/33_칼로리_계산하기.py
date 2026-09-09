menu = [400, 340, 170, 100, 70]
a, b = input().split()
result = menu[int(a) - 1] + menu[int(b) - 1]

print("angry" if result > 500 else "no angry")
