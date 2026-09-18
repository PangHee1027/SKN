from itertools import combinations
from collections import Counter

def solution(number):
    comb = [sum(i) for i in combinations(number, 3)]
    comb = Counter(comb)
    return comb[0]

# print(solution([-3, -2, -1, 0, 1, 2, 3]))