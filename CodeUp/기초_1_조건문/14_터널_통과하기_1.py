a, b, c = input().split()
passing = [int(a), int(b), int(c), 171]

print("PASS" if min(passing) == 171 else "CRASH")
