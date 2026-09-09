a, b = input().split()
a, b = int(a), int(b)

def donate(n) :
    return n / 2 * 10 if n % 2 == 0 else n // 2 + 1

print(int(donate(a) + donate(b)))
