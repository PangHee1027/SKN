def solution(d, budget):
    d.sort()
    for i, v in enumerate(d) :
        if budget < v :
            return i
        budget -= v
    return len(d)

print(solution([1,3,2,5,4], 9))