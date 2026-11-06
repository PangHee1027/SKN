n = int(input())
village = []

for i in range(n) :
    village.append(list(map(int, input().split())))

for i in range(1, n) :
    for j in range(3) :
        pre_cost = [x for x in village[i - 1]]
        pre_cost[j] = float('inf')
        village[i][j] += min(pre_cost)

print(min(village[-1]))
