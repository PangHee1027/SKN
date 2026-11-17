def solution(n, lost, reserve) :
    lost.sort()
    for d in set(lost) & set(reserve) :
        lost.remove(d)
        reserve.remove(d)
        
    delete = 0
    for i in lost :
        if i - 1 in reserve :
            delete += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve :
            delete += 1
            reserve.remove(i + 1)
            
    return n - (len(lost) - delete)