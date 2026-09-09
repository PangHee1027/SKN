a, b = input().split()

print(2012 - int(("19" + a[:2]) if (int(b) // 3 == 0) else ("20" + a[:2])) + 1)
 