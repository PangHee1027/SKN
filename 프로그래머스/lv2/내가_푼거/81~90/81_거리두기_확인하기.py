def solution(places):
    answer = []
    check = {(0, 1) : False, (0, -1) : False, (1, 0) : False, (-1, 0) : False, 
             (0, 2) : [(0, 1)], (0, -2) : [(0, -1)], (2, 0) : [(1, 0)], (-2, 0) : [(-1, 0)], 
             (1, 1) : [(0, 1), (1, 0)], (1, -1) : [(0, -1), (1, 0)], (-1, 1) : [(0, 1), (-1, 0)], (-1, -1) : [(0, -1), (-1, 0)]}
    
    for place in places :
        h = len(place)
        w = len(place[0])
        unable_place = False
        for i in range(h) :
            unable = False
            for j in range(w) :
                if place[i][j] == "P" :
                    for dx, dy in check.keys() :
                        x, y = i + dx, j + dy
                        if x < 0 or x >= h or y < 0 or y >= w :
                            continue
                        if place[x][y] in ("O", "X") :
                            continue
                        if not check[(dx, dy)] :
                            unable = True
                            break
                        checking = check.get((dx, dy))
                        u = False
                        for n, m in checking :
                            cx, cy = i + n, j + m
                            if place[cx][cy] in ("P", "O") :
                                u = True
                                break
                        if u :
                            unable = True
                            break
                if unable :
                    unable_place = True
                    break
            if unable_place :
                answer.append(0)
                break
        else :
            answer.append(1)
    return answer

print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
    )
)