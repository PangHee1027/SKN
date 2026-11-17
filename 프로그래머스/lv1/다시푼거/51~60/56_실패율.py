def solution(N, stages) :
    arrive = [0] * (N + 1)
    clear = [0] * (N + 1)
    
    for i in range(1, N + 1) :
        arrive[i] = sum(1 for s in stages if s >= i)
        clear[i] = sum(1 for s in stages if s > i)
    return sorted(range(1, N + 1), key = lambda i : (clear[i] / arrive[i]) if arrive[i] else 1)