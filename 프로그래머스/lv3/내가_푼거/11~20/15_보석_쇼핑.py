def solution(gems):
    left = 0
    n = len(gems)
    result = [0, n]
    gem_dict = {gem : 0 for gem in list(set(gems))}
    num_of_gem = len(gem_dict.items())
    gem_set = set()

    if len(gem_dict.keys()) == n :
        return [1, n]
    if len(gem_dict.keys()) == 1 :
        return [1, 1]

    for right in range(n) :
        gem_dict[gems[right]] += 1
        gem_set.add(gems[right])
        while len(gem_set) == num_of_gem :
            cur_gem = gems[left]
            gem_dict[cur_gem] -= 1
            if not gem_dict.get(cur_gem) :
                gem_set.remove(cur_gem)
            left += 1
            if result[1] - result[0] > right - left + 1 :
                result = [left, right + 1]
    
    return result

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))