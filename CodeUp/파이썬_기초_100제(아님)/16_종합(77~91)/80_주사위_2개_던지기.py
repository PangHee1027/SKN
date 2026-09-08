input_int1 , input_int2 = input().split()
input_int1 , input_int2 = int(input_int1), int(input_int2)

for i in range(1, input_int1 + 1) :
    for j in range(1, input_int2 + 1) :
        print(i, j)
