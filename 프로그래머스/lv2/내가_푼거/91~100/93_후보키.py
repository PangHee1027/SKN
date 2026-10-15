from itertools import combinations
from collections import deque

def solution(relation) :
    candiate_list = deque()
    candiate_key = []
    for i in range(1, len(relation[0]) + 1) :
        candiate_list += list(combinations(range(0, len(relation[0])), i))

    while candiate_list :
        cl = candiate_list.popleft()
        not_minimality = False
        for ck in candiate_key :
            if ck <= set(cl) :
                not_minimality = True
                break
        if not_minimality :
            continue
        l = []
        for row in relation :
            data = []
            for idx in cl :
                data.append(row[idx])
            l.append(tuple(data))

        if len(l) == len(set(l)) :
            candiate_key.append(set(cl))
        
    return len(candiate_key)

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))