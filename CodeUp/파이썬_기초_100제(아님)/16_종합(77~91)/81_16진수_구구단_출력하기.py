input_int = int(input(), 16)

for i in range(1, 0x10) : 
    result = input_int * i
    print(f"{'%X'%input_int}*{'%X'%i}={'%X'%result}")
