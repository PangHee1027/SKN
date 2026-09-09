a, b, c = input().split()
passing = [int(a), int(b), int(c)]

for i in passing :
    if i <= 170 :
        print("CRASH", i)
        break
else :
    print("PASS")
