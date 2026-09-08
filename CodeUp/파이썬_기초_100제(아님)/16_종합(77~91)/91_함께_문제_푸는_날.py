input_int1 , input_int2, input_int3 = input().split()
input_int1 , input_int2, input_int3 = int(input_int1), int(input_int2), int(input_int3)
result = 1

while(True) :
    if (result % input_int1 == 0 and result % input_int2 == 0 and result % input_int3 == 0) :
        break
    result += 1

print(result)
