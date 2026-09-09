a = input()
result = ""

if (int(a) % 10 == 1) :
    result = a + "st" if (int(a) // 10 != 1) else a + "th"
elif (int(a) % 10 == 2) :
    result = a + "nd" if (int(a) // 10 != 1) else a + "th"
elif (int(a) % 10 == 3) :
    result = a + "rd" if (int(a) // 10 != 1) else a + "th"
else :
    result = a + "th"

print(result)
