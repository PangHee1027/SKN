from collections import Counter

def solution(topping):
    s = set()
    c = Counter(topping)
    answer = 0
    for t in topping :
        s.add(t)
        c[t] -= 1
        if not c[t] :
            del c[t]
        if len(s) == len(c.keys()) :
            answer += 1
            continue
        if answer :
            break
    return answer