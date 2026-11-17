def solution(string) :
    alpha_dict = {}
    answer = []
    for i, s in enumerate(string) :
        answer.append(i - alpha_dict.get(s, i + 1))
        alpha_dict[s] = i
    
    return answer