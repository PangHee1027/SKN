def solution(scores):
    wanho = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1]))
    survived = []
    limit_b = scores[0][1]
    
    for score in scores :
        if score[1] < limit_b :
            if score == wanho :
                return -1
            continue
        else :
            survived.append(sum(score))
            limit_b = score[1]

    survived.sort(reverse=True)

    return survived.index(sum(wanho)) + 1

print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))