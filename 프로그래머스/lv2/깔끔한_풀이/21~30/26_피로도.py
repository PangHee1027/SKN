from itertools import permutations

def solution(k, dungeons):
    maximum = 0
    total_dungeons = len(dungeons)
    
    # 1. list() 변환 없이 제너레이터 직접 순회
    for dungeon_list in permutations(dungeons):
        tired = k
        cur = 0
        
        for min_tired, consumed in dungeon_list:
            if tired >= min_tired:
                tired -= consumed
                cur += 1
            else:
                break
                
        maximum = max(maximum, cur)
        
        # 2. 모든 던전을 탐험할 수 있는 경우 조기 종료
        if maximum == total_dungeons:
            return maximum
            
    return maximum