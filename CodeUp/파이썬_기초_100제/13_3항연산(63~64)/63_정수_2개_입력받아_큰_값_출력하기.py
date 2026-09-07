input_int1, input_int2 = input().split()
input_int1, input_int2 = int(input_int1), int(input_int2)
output_int = input_int1 if (input_int1 >= input_int2) else input_int2
print(output_int)