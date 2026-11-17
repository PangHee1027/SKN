from collections import Counter

def solution(X, Y):
    c1, c2 = Counter(X), Counter(Y)
    c = c1 & c2
    if not c :
        return '-1'
    result = []
    for k, v in c.items() :
        result += [int(k)] * v
    if not max(result) :
        return '0'
    
    result.sort(reverse = True)
    return "".join(map(str, result))