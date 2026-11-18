def solution(players, callings) :
    def swap(i) :
        rank[players[i]] -= 1
        rank[players[i - 1]] += 1
        players[i], players[i - 1] = players[i - 1], players[i]
        
    rank = {p : i for i, p in enumerate(players)}
    
    for call in callings :
        cur = rank[call]
        swap(cur)
    
    return sorted(list(rank.keys()), key = lambda x : rank[x])