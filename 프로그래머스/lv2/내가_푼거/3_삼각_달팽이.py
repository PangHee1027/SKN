def solution(n):
    triangle = [[0] * i for i in range(1, n + 1)]
    answer = []

    dr, dc = [1, 0, -1], [0, 1, -1]
    current_direction = 0

    coordinate = [0, 0]

    for i in range(1, sum(range(1, n + 1)) + 1) :
        triangle[coordinate[0]][coordinate[1]] = i
        next_coordinate = [coordinate[0] + dr[current_direction], coordinate[1] + dc[current_direction]]
        if next_coordinate[0] < n and next_coordinate[1] < n and triangle[next_coordinate[0]][next_coordinate[1]] == 0 :
            coordinate = [next_coordinate[0], next_coordinate[1]]
        else :
            current_direction = (current_direction + 1) % 3
            coordinate = [coordinate[0] + dr[current_direction], coordinate[1] + dc[current_direction]]

    for i in triangle :
        answer += i
    return answer

# print(solution(5))