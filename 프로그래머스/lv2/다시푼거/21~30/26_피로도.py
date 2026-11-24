from itertools import permutations

def solution(k, dungeons) :
    n = len(dungeons)
    max_dungeon = 0
    for p in permutations(dungeons, n) :
        tired = k
        for i, (require, cost) in enumerate(p) :
            if require > tired :
                max_dungeon = max(max_dungeon, i)
                break
            tired -= cost
        else :
            return n
    return max_dungeon