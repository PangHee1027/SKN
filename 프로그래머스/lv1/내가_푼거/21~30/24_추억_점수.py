def solution(name, yearning, photos):
    score_dic = dict(zip(name, yearning))
    answer = []

    for photo in photos :
        photo_score = 0
        for person in photo :
            photo_score += score_dic.get(person) if score_dic.get(person) else 0
        answer.append(photo_score)
    
    return answer

# print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))