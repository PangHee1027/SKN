def solution(mats, park):
    mats.sort(reverse=True)
    for i in range(len(park)) :
        for j in range(len(park[i])) :
            if park[i][j] != "-1" :
                continue
            for m in mats :
                can_place = True
                if i + m > len(park) + 1 or j + m > len(park[i]) + 1 :
                    continue
                for k in range(i, i + m) :
                    for l in range(j, j + m) :
                        if park[k][l] != "-1" :
                            can_place = not can_place
                            break
                if can_place :
                    return m 
    return - 1

print(solution([5, 5, 1],
         [["A", "A", "-1", "B", "B", "B", "B", "-1"],
          ["A", "A", "-1", "B", "B", "B", "B", "-1"],
          ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
          ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
          ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
          ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"]]))