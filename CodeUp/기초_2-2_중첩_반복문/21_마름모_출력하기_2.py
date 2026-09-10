a = int(input())

for i in range(a - 1, -1, -1) :
   print(" " * i + "*" * (2 * (a - i) - 1) + " " * i)

for i in range(1, a) :
   print(" " * i + "*" * (2 * (a - i) - 1) + " " * i)
