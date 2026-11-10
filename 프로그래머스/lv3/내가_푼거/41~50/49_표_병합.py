def solution(commands) :
    def find_root(r, c) :
        while isinstance(table[r][c], tuple) :
            r, c = table[r][c]
        return r, c
    empty = 'EMPTY'
    table = [['EMPTY'] * 51 for _ in range(51)]
    merged = {}
    answer = []
    for command in commands :
        command = command.split()
        match command[0] :
            case 'UPDATE' :
                if len(command) == 4 :
                    r, c, v = int(command[1]), int(command[2]), command[3]
                    r, c = find_root(r, c)
                    table[r][c] = v
                else :
                    v1, v2 = command[1], command[2]
                    for i in range(1, 51) :
                        for j in range(1, 51) :
                            if table[i][j] == v1 :
                                table[i][j] = v2
            case 'MERGE' :
                r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
                r1, c1 = find_root(r1, c1)
                r2, c2 = find_root(r2, c2)
                if r1 == r2 and c1 == c2 :
                    continue
                value = empty
                if table[r1][c1] != empty :
                    value = table[r1][c1]
                elif table[r2][c2] != empty :
                    value = table[r2][c2]
                table[r1][c1] = value
                table[r2][c2] = (r1, c1)
            case 'UNMERGE' :
                r, c = int(command[1]), int(command[2])
                root_r, root_c = find_root(r, c)
                value = table[root_r][root_c]
                merged_cells = []
                for i in range(1, 51) :
                    for j in range(1, 51) :
                        if find_root(i, j) == (root_r, root_c) :
                            merged_cells.append((i, j))
                for finded_r, finded_c in merged_cells :
                    table[finded_r][finded_c] = empty
                table[r][c] = value
            case 'PRINT' :
                r, c = int(command[1]), int(command[2])
                r, c = find_root(r, c)
                value = table[r][c]
                answer.append(value)
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))