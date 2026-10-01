def solution(citations):
    if len(citations) == 0 or max(citations) == 0 :
        return 0
    if min(citations) >= len(citations) :
        return len(citations)
    
    idx = sorted(citations, reverse = True)
    for i, value in enumerate(idx) :
        if i >= value and i >= len(idx) - i:
            return i

print(solution([3, 4]))