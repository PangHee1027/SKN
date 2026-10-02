def solution(dirs):
    dir = {"U" : (0, 1), "D" : (0, -1), "L" : (-1, 0), "R" : (1, 0)}
    visited = set()
    cur_coor = [0, 0]
    answer = 0
    for c in dirs :
        direction = dir[c]
        target_coor = [cur_coor[0] + direction[0], cur_coor[1] + direction[1]]
        if not (-5 <= target_coor[0] <= 5 and -5 <= target_coor[1] <= 5) :
            continue
        if not tuple(zip(cur_coor, target_coor)) in visited :
            visited.add(tuple(zip(cur_coor, target_coor)))
            visited.add(tuple(zip(target_coor, cur_coor)))
            answer += 1
        cur_coor = target_coor
    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))