input()
a = input()
count_A = 0
count_B = 0
result = ""

for i in range(len(a)) :
    if a[i] == "A" :
        count_A += 1
    elif a[i] == "B" :
        count_B += 1
    else :
        print("무효표 발생")

if count_A > count_B :
    result = "A"
elif count_A < count_B :
    result = "B"
else :
    result = "Tie"

print(result)
