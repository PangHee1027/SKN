input_int = int(input())

def has_369(int1) :
    string1 = str(int1)
    result = 0
    for s in string1 :
        if (s == "3" or s == "6" or s == "9") :
            result += 1
    return result


for i in range(1, input_int + 1) :
    repeat = has_369(i)
    if (not repeat) :
        print(i, end = " ")
    else :
        print("X" * repeat, end = " ")
