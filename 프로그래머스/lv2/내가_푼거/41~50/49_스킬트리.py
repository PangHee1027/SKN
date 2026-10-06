from collections import deque

def solution(skill, skill_trees):
    skills = []
    for i in range(len(skill)) :
        skills.append(skill[i])

    answer = 0
    for skill_tree in skill_trees :
        skill_order = deque(skills)
        for skill in skill_tree :
            if skill not in skills :
                continue
            if skill != skill_order.popleft() :
                break
        else :
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))