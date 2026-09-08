red, green, blue = input().split()
red, green, blue = int(red), int(green), int(blue)
repeat = 0

for i in range(red) :
    for j in range(green) :
        for k in range(blue) :
            print(i, j, k)
            repeat += 1
print(repeat)
