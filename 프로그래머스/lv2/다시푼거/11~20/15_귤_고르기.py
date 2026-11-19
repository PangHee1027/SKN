from collections import Counter

def solution(k, tangerine) :
    count = Counter(tangerine)
    tangerine.sort(key = lambda x : (-count[x], x))
    
    return len(set(tangerine[:k]))
    