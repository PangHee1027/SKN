def solution(mats, park):
    H, W = len(park), len(park[0])
    mats.sort(reverse = True)

    for size in mats :
        for i in range(H - size + 1) :
            for j in range(W - size + 1) :
                can_place = True
                if park[i][j] != "-1" :
                    continue
                for k in range(i, i + size) :
                    for l in range(j, j + size) :
                        if park[k][l] != "-1" :
                            can_place = False
                            break
                if can_place :
                    return size
    return -1

print(solution([2, 5, 3],
         [["A", "A", "-1", "B", "B", "B", "B", "-1"],
          ["A", "A", "-1", "B", "B", "B", "B", "-1"],
          ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
          ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
          ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
          ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"]]))