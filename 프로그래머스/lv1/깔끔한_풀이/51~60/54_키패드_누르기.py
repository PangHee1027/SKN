def solution(numbers, hand):
    keypad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        "*": (3, 0),
        0: (3, 1),
        "#": (3, 2),
    }

    # 맨해튼 거리 계산 함수
    def get_dist(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    left_pos, right_pos = "*", "#"
    result = []

    for num in numbers:
        if num in (1, 4, 7):
            move = "L"
        elif num in (3, 6, 9):
            move = "R"
        else:
            l_dist = get_dist(keypad[num], keypad[left_pos])
            r_dist = get_dist(keypad[num], keypad[right_pos])

            if l_dist < r_dist:
                move = "L"
            elif l_dist > r_dist:
                move = "R"
            else:
                move = "L" if hand == "left" else "R"

        # 결정된 손에 따라 위치 즉시 업데이트
        if move == "L":
            left_pos = num
        else:
            right_pos = num

        result.append(move)

    return "".join(result)