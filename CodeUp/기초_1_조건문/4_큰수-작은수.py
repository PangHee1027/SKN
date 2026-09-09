input_int1 , input_int2 = input().split()
input_int1 , input_int2 = int(input_int1), int(input_int2)

print(input_int1 - input_int2 if input_int1 >= input_int2 else input_int2 - input_int1)
