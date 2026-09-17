def solution(friends, gifts):
    gift_point = {i : 0 for i in friends}
    gift_dict = {i : 0 for i in gifts}
    present_dict = {i : 0 for i in friends}

    for i in gifts :
        gift_dict[i] += 1
        i = i.split()
        gift_point[i[0]] += 1
        gift_point[i[1]] -= 1

    count = 0
    for i in range(len(friends)) :
        for j in range(i + 1, len(friends)) :
            a = gift_dict.get(friends[i] + " " + friends[j])
            b = gift_dict.get(friends[j] + " " + friends[i])
            if not a or not b :
                if a :
                    present_dict[friends[i]] += 1
                elif b :
                    present_dict[friends[j]] += 1
                else :
                    if gift_point[friends[i]] > gift_point[friends[j]] :
                        present_dict[friends[i]] += 1
                    elif gift_point[friends[i]] < gift_point[friends[j]] :
                        present_dict[friends[j]] += 1
            elif a < b :
                present_dict[friends[j]] += 1
            elif a > b :
                present_dict[friends[i]] += 1
            else :
                if gift_point[friends[i]] > gift_point[friends[j]] :
                    present_dict[friends[i]] += 1
                elif gift_point[friends[i]] < gift_point[friends[j]] :
                    present_dict[friends[j]] += 1
    print(gift_dict)
    return max(present_dict.values())

# print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))