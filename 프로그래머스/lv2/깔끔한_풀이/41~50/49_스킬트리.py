def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        # 1. skill에 들어있는 선행 스킬들만 순서대로 추출
        filtered_skills = "".join([s for s in tree if s in skill])
        
        # 2. skill이 추출된 문자열로 시작하는지 확인
        if skill.startswith(filtered_skills):
            answer += 1
            
    return answer