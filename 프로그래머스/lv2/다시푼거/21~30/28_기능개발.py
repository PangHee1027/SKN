from collections import Counter

def solution(progresses, speeds) :
    require = []
    for p, s in zip(progresses, speeds) :
        i = (100 - p + s - 1) // s
        if require and require[-1] >= i :
            require.append(require[-1])
        else :
            require.append(i)
            
    return list(Counter(require).values())