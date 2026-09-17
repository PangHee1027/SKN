def solution(park, routes):
    coordinate = [0, 0]
    h = len(park)
    w = len(park[0])

    for i in range(h) :
        for j in range(w) :
            if park[i][j] == "S" :
                coordinate = [i, j]
                break
        else:
            continue
        break

    for i in routes :
        dir, dif = i.split()
        dif = int(dif)
        match dir :
            case "S" :
                if coordinate[0] + dif >= h :
                    continue 
                for j in range(coordinate[0], coordinate[0] + dif + 1) :
                    if park[j][coordinate[1]] == "X" :
                        break
                else :
                    coordinate[0] += dif
            case "E" :
                if coordinate[1] + dif >= w :
                    continue 
                for j in range(coordinate[1], coordinate[1] + dif + 1) :
                    if park[coordinate[0]][j] == "X" :
                        break
                else :
                    coordinate[1] += dif
            case "N" :
                if coordinate[0] - dif < 0 :
                    continue 
                for j in range(coordinate[0], coordinate[0] - dif - 1, -1) :
                    if park[j][coordinate[1]] == "X" :
                        break
                else :
                    coordinate[0] -= dif
            case "W" :
                if coordinate[1] - dif < 0 :
                    continue 
                for j in range(coordinate[1], coordinate[1] - dif - 1, -1) :
                    if park[coordinate[0]][j] == "X" :
                        break
                else :
                    coordinate[1] -= dif

    return coordinate

# print(solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"]))