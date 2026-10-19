from collections import Counter

def solution(points, routes):
    def move(cur_coor, target) :
        r, c = cur_coor
        t_r, t_c = points_dict[target]
        r_dif = t_r - r
        if r_dif :
            if r_dif > 0 :
                return (r + 1, c)
            else :
                return (r - 1, c)
        c_dif = t_c - c
        if c_dif > 0 :
            return (r, c + 1)
        else :
            return (r, c - 1)
        
    points_dict = {}
    for i, point in enumerate(points) :
        points_dict[i + 1] = (point[0] - 1, point[1] - 1)

    robots = [[points_dict[route[0]], route[1:][::-1]] for route in routes]
    crash = sum(1 for x in Counter(y[0] for y in robots).values() if x > 1)
    arrive = [0 for _ in range(len(robots))]

    while True :
        for i, robot in enumerate(robots) :
            if arrive[i] :
                robot[0] = (100 + i, 100 + i)
                continue
            target = robot[1][-1]
            cur = robot[0]
            robot[0] = move(cur, target)
            if robot[0] == points_dict[target] :
                if len(robot[1]) > 1 :
                    robot[1].pop()
                    target = robot[1][-1]
                else :
                    arrive[i] = 1
                    continue
        crash += sum(1 for x in Counter(y[0] for y in robots).values() if x > 1)
        if all(arrive) :
            break
   
    return crash

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])) # 1
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])) # 9
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])) # 0
#print(solution([[1, 1], [1, 3]], [[1, 2, 1, 2], [2, 1, 2, 1]])) # 3
#print(solution([[1, 1], [2, 2], [3, 3]], [[1, 2, 1], [3, 2, 1]])) # 3
#print(solution([[1, 1], [1, 2], [2, 1]], [[1, 2], [1, 3, 2], [1, 3]]))
