from itertools import combinations

def solution(line):
    meet = set()
    count_of_line = len(line)

    for (A, B, E), (C, D, F) in combinations(line, 2):
        x_child = B * F - E * D
        x_parent = A * D - B * C
        y_child = E * C - A * F
        y_parent = A * D - B * C
        if x_parent == 0 or y_parent == 0:
            continue
        if x_child % x_parent :
            continue
        if y_child % y_parent :
            continue
        x, y = x_child // x_parent, y_child // y_parent

        meet.add((x, y))

    meet = list(meet)
    correction_x = -min(x[0] for x in meet)
    correction_y = -min(y[1] for y in meet)

    for i, coor in enumerate(meet) :
        x, y = coor
        x += correction_x
        y += correction_y
        meet[i] = (x, y)

    max_x = max(x[0] for x in meet)
    max_y = max(y[1] for y in meet)

    board = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y in meet :
        board[y][x] = "*"

    for i, row in enumerate(board) :
        board[i] = "".join(row)

    return board[::-1]

#print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
#print(solution([[1, -1, 0], [2, -1, 0]]))
#print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))