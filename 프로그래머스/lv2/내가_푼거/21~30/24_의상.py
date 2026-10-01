def solution(clothes):
    clothes_dict = {}
    for cloth, category in clothes :
        if clothes_dict.get(category) :
            clothes_dict[category] += [cloth]
        else :
            clothes_dict[category] = [cloth]
    answer = 1
    for l in clothes_dict.values() :
        answer *= len(l) + 1
    return answer - 1

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))