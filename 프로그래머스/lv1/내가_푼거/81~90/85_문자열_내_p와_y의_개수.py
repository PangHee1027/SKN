from collections import Counter

def solution(s):
    s = s.lower()
    c1 = Counter(s)
    return c1["p"] == c1["y"]

print(solution("pPoooyY"))