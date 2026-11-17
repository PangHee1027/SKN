from itertools import combinations

def solution(number):
    return [sum(combination) for combination in combinations(number, 3)].count(0)