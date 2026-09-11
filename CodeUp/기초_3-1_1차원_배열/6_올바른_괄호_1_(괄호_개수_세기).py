a = input()
count1, count2 = 0, 0

for i in range(len(a)) :
    if a[i] == "(" :
        count1 += 1
    elif a[i] == ")" :
        count2 += 1

print(count1, count2)
