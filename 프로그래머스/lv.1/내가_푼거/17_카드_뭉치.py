def solution(cards1, cards2, goal):
    goal_dict = {i : 1 for i in range(len(goal))}
    cards1_index = []
    cards2_index = []

    for i in range(len(goal)) :
        if goal_dict[i] == 1 and goal[i] in cards1 :
            goal_dict[i] = 0
            cards1_index.append(cards1.index(goal[i]))
            if max(cards1_index) != cards1_index[-1] :
                return "No"
        if goal_dict[i] == 1 and goal[i] in cards2 :
            goal_dict[i] = 0
            cards2_index.append(cards2.index(goal[i]))
            if max(cards2_index) != cards2_index[-1] :
                return "No"
    print(cards1_index)
    print(cards2_index)
    for i in range(len(cards1_index)) :
        if i != cards1_index[i] :
            return "No"
    for i in range(len(cards2_index)) :
        if i != cards2_index[i] :
            return "No"

    return "Yes"

# print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))