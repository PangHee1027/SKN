def solution(citations):
    n = len(citations)
    citations.sort(reverse = True)
    for i, c in enumerate(citations) :
        if i >= c :
            return i
    return n