from bisect import bisect_left
from itertools import product
from collections import defaultdict

def solution(info, query):
    participant = defaultdict(list)
    answer = []

    for i in info :
        i = i.split(" ")
        dict = [{0 : "-", 1 : i[0]}, {0 : "-", 1 : i[1]}, {0 : "-", 1 : i[2]}, {0 : "-", 1 : i[3]}]
        score = int(i[4])
        for a, b, c, d in product(range(2), repeat = 4) :
            participant[(dict[0][a], dict[1][b], dict[2][c], dict[3][d])] += [score]

    for key, value in participant.items() :
        participant[key] = sorted(value)

    for q in query :
        q = q.replace("and", "").split()
        score_limit = int(q[4])
        satisfy = participant.get(tuple(q[:4]), [])
        result = len(satisfy) - bisect_left(satisfy, score_limit)
        answer.append(result)

    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
# [1, 1, 1, 1, 2, 4]