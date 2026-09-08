checkerboard = [[0 for i in range(19)] for j in range(19)]

for i in range(19) :
    input_row = input().split()
    for j in range(len(input_row)) :
        checkerboard[i][j] = int(input_row[j])

repeat = int(input())

for i in range(repeat) :
    current_coordinate = input().split()
    for j in range(len(current_coordinate)) :
        current_coordinate[j] = int(current_coordinate[j]) - 1
    for j in range(19) :
        checkerboard[current_coordinate[0]][j] = int(not checkerboard[current_coordinate[0]][j])
    for j in range(19) :
        checkerboard[j][current_coordinate[1]] = int(not checkerboard[j][current_coordinate[1]])

for i in range(19) :
    for j in range(19) :
        print(checkerboard[i][j], end = " ")
    print()
    