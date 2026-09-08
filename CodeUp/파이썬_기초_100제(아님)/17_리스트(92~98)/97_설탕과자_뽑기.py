input_int1 , input_int2 = input().split()
checkerboard = [[0 for i in range(int(input_int2))] for i in range(int(input_int1))]
repeat = int(input())

for i in range(repeat) :
    stick_info = input().split()
    long = int(stick_info[0])
    direction = int(stick_info[1])
    start_coordinate = [int(stick_info[2]) - 1, int(stick_info[3]) - 1]

    if (direction) :
        for j in range(start_coordinate[0], start_coordinate[0] + long) :
            checkerboard[j][start_coordinate[1]] = 1
    else :
        for j in range(start_coordinate[1], start_coordinate[1] + long) :
            checkerboard[start_coordinate[0]][j] = 1
            
for i in range(int(input_int1)) :
    for j in range(int(input_int2)) :
        print(checkerboard[i][j], end = " ")
    print()
