def solution(storey):
    storey = list(map(int, list(str(storey))))
    storey.reverse()
    n = len(storey)
    answer = 0
    for i, s in enumerate(storey) :
        nxt = 0
        if s < 5 :
            answer += s
        elif s > 5 :
            answer += 10 - s
            nxt += 1
        else :
            answer += 5
            if i != n - 1 :
                if storey[i + 1] >= 5 :
                    nxt += 1
        if i == n - 1 :
            answer += nxt
        else :
            storey[i + 1] += nxt
    
    return answer