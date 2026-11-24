import re

def solution(skill, skill_trees):
    pattern = '|'.join(list(skill))
    answer = 0
    for skill_tree in skill_trees :
        if skill.startswith(''.join(re.findall(pattern, skill_tree))) :
            answer += 1
    return answer