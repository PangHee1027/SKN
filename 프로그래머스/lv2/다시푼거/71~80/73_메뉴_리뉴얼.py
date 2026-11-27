from itertools import combinations
from collections import Counter

def solution(orders, course) :
    orders = list(map(list, orders))
    answer = []
    for n in course :
        counter = Counter([])
        for order in orders :
            counter += Counter(list(map(frozenset, combinations(order, n))))
        if not counter :
            continue
            
        max_count = max(list(counter.values()) + [2])
        result = [''.join(sorted(list(x))) for x in counter.keys() if counter[x] == max_count]
        answer += result
    
    return sorted(answer)