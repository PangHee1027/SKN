def solution(n, costs):
    parent_island = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    cost = 0

    if n == 1 :
        return 0

    for i1, i2, c in costs :
        p1, p2 = parent_island[i1], parent_island[i2]

        if p1 != p2 :
            cost += c
            for i, p in enumerate(parent_island) :
                if p == p2 :
                    parent_island[i] = p1

    return cost

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))