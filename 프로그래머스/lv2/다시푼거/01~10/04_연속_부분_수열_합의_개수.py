def solution(elements):
    s = set()
    n = len(elements)
    
    elements *= 2
    
    for i in range(n) :
        for j in range(2 * n - i) :
            s.add(sum(elements[j : j + i]))
    return len(s)