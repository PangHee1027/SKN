a = int(input())

for i in range(1, a + 1) :
    if i % 2 == 1 :
        print(" " * ((a - i) // 2) + "*" * i + " " * ((a - i) // 2))
