from itertools import permutations

def solution(k, dungeons):
    dungeon_list_permutation = list(permutations(dungeons))
    maximum = 0
    for dungeon_list in dungeon_list_permutation :
        tired = k
        cur = 0
        for dungeon in dungeon_list :
            if tired < dungeon[0] :
                maximum = max(maximum, cur)
                break
            else :
                tired -= dungeon[1]
                cur += 1
        else :
            maximum = max(maximum, cur)
    
    return maximum

print(solution(80, [[80,20],[50,40],[30,10]]))