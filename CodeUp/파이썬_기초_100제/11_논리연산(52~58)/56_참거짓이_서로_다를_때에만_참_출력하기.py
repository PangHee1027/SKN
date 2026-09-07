input_int1, input_int2 = input().split()
input_bool1, input_bool2 = bool(int(input_int1)), bool(int(input_int2))
output_bool = (input_bool1 and (not input_bool2)) or ((not input_bool1) and input_bool2)
print(output_bool)