def solution(picks, minerals):
    tired = {"diamond" : [1, 5, 25], "iron" : [1, 1, 5], "stone" : [1, 1, 1]}
    dia, iron, stone = picks
    works = [minerals[i : i + 5] for i in range(0, len(minerals), 5)]
    if len(works) > sum(picks) :
        works = works[:sum(picks)]

    for i, work in enumerate(works) :
        t = [0, 0, 0]
        for mine in work :
            for j in range(3) :
                t[j] += tired[mine][j]
        works[i] = t

    works.sort(key = lambda x : x[2], reverse = True)
    answer = 0

    for work in works :
        if dia :
            answer += work[0]
            dia -= 1
            continue
        if iron :
            answer += work[1]
            iron -= 1
            continue
        answer += work[2]
        stone -= 1
        
    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))