from itertools import combinations

def solution(number):
    comb_sums = [sum(c) for c in combinations(number, 3)]
    return comb_sums.count(0)