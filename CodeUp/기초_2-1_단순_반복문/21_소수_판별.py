a = int(input())
count = 0

for i in range(1, a + 1) :
    count += 1 if a % i == 0 else 0

print("prime" if count == 2 else "not prime")
