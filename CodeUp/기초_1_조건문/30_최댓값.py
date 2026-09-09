a, b = input().split()
a, b = float(a), float(b)

sum, mult, sub1, sub2, div1, div2, pow1, pow2 = a + b, a * b, a - b, b - a, a / b, b / a, a ** b, b ** a
list1 = [sum, mult, sub1, sub2, div1, div2, pow1, pow2]

print(format(max(list1), "0.6f"))
