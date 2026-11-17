def solution(d, budget):
    d.sort()
    n = len(d)
    for i, x in enumerate(d) :
        budget -= x
        if budget < 0 :
            return i
    return n