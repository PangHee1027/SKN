def solution(name, yearning, photo):
    score_dic = dict(zip(name, yearning))
    answer = []

    for p in photo:
        # get(person, 0)을 사용해 없는 인물은 0점으로 합산
        photo_score = sum(score_dic.get(person, 0) for person in p)
        answer.append(photo_score)
    
    return answer