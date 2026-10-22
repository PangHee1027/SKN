def solution(m, n, startX, startY, balls) :
    answer = []
    for x, y in balls :
        cases = []
        for dx, dy in ((x, -y), (x, 2 * n - y), (-x, y), (2 * m - x, y)) :
            distance = (startX - dx) ** 2 + (startY - dy) ** 2
            cases.append(distance)
        if startX == x :
            if y < startY :
                cases[0] = float("inf")
            else :
                cases[1] = float("inf")

        if startY == y :
            if x < startX :
                cases[2] = float("inf")
            else :
                cases[3] = float("inf")

        if startX * (startY - y) == startY * (startX - x) :
            distance = float('inf')
            if startX < x :
                distance = (startX + x) ** 2 + (startY  + y) ** 2
            else :
                distance = (startX - (2 * m - x)) ** 2 + (startY  - (2 * n - y)) ** 2
            cases.append(distance)
        answer.append(min(cases))

    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))