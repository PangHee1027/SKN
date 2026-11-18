from collections import Counter

def solution(participant, completion) :
    c1, c2 = Counter(participant), Counter(completion)
    c = c1 - c2
    return list(c.keys())[0]