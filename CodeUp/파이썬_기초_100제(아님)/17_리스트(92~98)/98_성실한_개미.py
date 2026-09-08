box = [[0 for i in range(10)] for j in range(10)]
ant_right = True
ant_coordinate = [1, 1]
is_stucked = False

def next_coordiante(b, r, c) :
    if (b[c[0]][c[1] + 1] != 1) :
        r = True 
    if (r) :
        return b[c[0]][c[1] + 1], r
    else :
        return b[c[0] + 1][c[1]], r

def ant_move(b, r, c):
    if (r) :
        c[1] += 1
    else :
        c[0] +=1
    b[c[0]][c[1]] = 9    
    return c

def check_stuck(b, c) :
    if (b[c[0]][c[1] + 1] == 1 and b[c[0] + 1][c[1]] == 1) :
        return True
    else :
        return False

for i in range(10) :
    input_row = input().split()
    for j in range(len(input_row)) :
        box[i][j] = int(input_row[j])

box[1][1] = 9

while (not is_stucked) :
    next_coor, ant_right = next_coordiante(box, ant_right, ant_coordinate)
    if (next_coor == 2) :
        ant_move(box, ant_right, ant_coordinate)
        break
    elif (next_coor == 1) :
        ant_right = not ant_right
    else :
        ant_move(box, ant_right, ant_coordinate)
    is_stucked = check_stuck(box, ant_coordinate)

for i in range(10) :
    for j in range(10) :
        print(box[i][j], end = " ")
    print()
