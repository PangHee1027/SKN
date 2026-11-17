from collections import defaultdict

def solution(name, yearning, photo):
    yearning_dict = defaultdict(int) | {n : y for n, y in zip(name, yearning)}
    answer = []
    for p in photo :
        answer.append(sum(yearning_dict[n] for n in p))
    return answer