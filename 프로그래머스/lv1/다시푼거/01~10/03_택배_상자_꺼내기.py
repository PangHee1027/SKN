def solution(n, w, num) :
    position = [-1] + [(w - (i % w) + 1) % w if ((i + w - 1) // w - 1) % 2 else i % w for i in range(1, n + 1)]
    target = position[num]
    return sum(1 for i in range(num, n + 1) if position[i] == target)