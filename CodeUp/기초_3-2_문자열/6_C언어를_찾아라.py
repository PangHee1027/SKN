a = input().lower()
c_count = 0
cc_count = 0

for i in range(len(a)) :
    if a[i] == "c" :
        c_count += 1
        if i != 0 and a[i - 1] == "c" :
            cc_count += 1

print(c_count, cc_count, sep = "\n")
