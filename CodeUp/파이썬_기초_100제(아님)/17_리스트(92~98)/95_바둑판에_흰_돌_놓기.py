checkerboard = [[0 for i in range(19)] for j in range(20)]
repeat = int(input())

while (repeat) :
    current_coordinate = input().split()
    for i in range(len(current_coordinate)) :
        current_coordinate[i] = int(current_coordinate[i])
    #if (checkerboard[current_coordinate[0] - 1][current_coordinate[1] - 1]) :
    #    print("이미 바둑돌이 존재합니다. 다시 위치를 지정해주세요")
    #else :
    #    checkerboard[current_coordinate[0] - 1][current_coordinate[1] - 1] = 1
    #    repeat -= 1
    checkerboard[current_coordinate[0] - 1][current_coordinate[1] - 1] = 1
    repeat -= 1

for i in range(19) :
    for j in range(19) :
        print(checkerboard[i][j], end = " ")
    print()
