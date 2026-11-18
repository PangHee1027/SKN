def solution(park, routes) :
    coor = [-1, -1]
    obstacle = set()
    n, m = len(park), len(park[0])
    
    for i in range(n) :
        for j in range(m) :
            if park[i][j] == 'S' :
                coor = [i, j]
            elif park[i][j] == 'X' :
                obstacle.add((i, j))
    for route in routes :
        direction, distance = route.split()
        distance = int(distance)
        x, y = coor
        match direction :
            case 'N' :
                nx = x - distance
                if nx < 0 :
                    continue
                if any((i, y) in obstacle for i in range(nx, x)) :
                    continue    
                coor[0] = nx
            case 'S' :
                nx = x + distance
                if nx >= n :
                    continue
                if any((i, y) in obstacle for i in range(x, nx + 1)) :
                    continue
                coor[0] = nx
            case 'E' :
                ny = y + distance
                if ny >= m :
                    continue
                if any((x, i) in obstacle for i in range(y, ny + 1)) :
                    continue
                coor[1] = ny
            case 'W' :
                ny = y - distance
                if ny < 0 :
                    continue
                if any((x, i) in obstacle for i in range(ny, y)) :
                    continue
                coor[1] = ny
    
    return coor