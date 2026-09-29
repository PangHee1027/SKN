def solution(participant, completion):
    completion_dict = {name : 0 for name in completion}
    for name in completion :
        completion_dict[name] += 1
    for name in participant :
        if not (completion_dict.get(name)) :
            return name
        if completion_dict.get(name) == 0 :
            return name
        completion_dict[name] -= 1

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))