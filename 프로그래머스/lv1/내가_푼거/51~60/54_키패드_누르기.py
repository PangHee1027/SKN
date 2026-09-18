def solution(numbers, hand):
    keypad_coordinate = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2), 4 : (1, 0), 5 : (1, 1), 6 : (1, 2), 7 : (2, 0), 8 : (2, 1), 9 : (2, 2), "*" : (3, 0), 0 : (3, 1), "#" : (3, 2)}
    left, right = "*", "#"
    answer = ''
    for i in numbers :
        if i in (1, 4, 7) :
            answer += "L"
        elif i in (3, 6, 9) :
            answer += "R"
        else :
            left_distance = abs(keypad_coordinate[i][0] - keypad_coordinate[left][0]) + abs(keypad_coordinate[i][1] - keypad_coordinate[left][1])
            right_distance = abs(keypad_coordinate[i][0] - keypad_coordinate[right][0]) + abs(keypad_coordinate[i][1] - keypad_coordinate[right][1])
            if left_distance > right_distance :
                answer += "R"
            elif left_distance < right_distance :
                answer += "L"
            else :
                if hand == "left" :
                    answer += "L"
                else :
                    answer += "R"
        if answer[-1] == "L" :
            left = i
        else :
            right = i
    return answer

# print(solution([0, 0], "right"))