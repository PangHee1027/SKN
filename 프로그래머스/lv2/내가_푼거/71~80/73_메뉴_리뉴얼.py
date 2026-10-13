from itertools import combinations

def solution(orders, course):
    for i, order in enumerate(orders) :
        orders[i] = set(order)

    intersect = {}

    for i, order in enumerate(orders) :
        for j in range(i + 1, len(orders)) :
            l = sorted(list(order.intersection(orders[j])))
            for k in course : 
                if k <= len(l) :
                    for m in combinations(l, k) :
                        m = "".join(m)
                        intersect[m] = intersect.get(m, 0) + 1

    answer = []

    for i in course :
        max_count = 0
        cur = []
        for candidate in intersect.keys() :
            if len(candidate) == i :
                count = intersect.get(candidate)
                if count  > max_count :
                    cur = [candidate]
                    max_count = count
                elif count== max_count :
                    cur.append(candidate)
        answer += cur
   
    return sorted(answer)

#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
#print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))