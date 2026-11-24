from collections import Counter

def solution(s):
    s = list(map(int, s.replace('{', '').replace('}', '').split(',')))
    c = Counter(s)
    
    return sorted(c.keys(), key = lambda x : -c[x])