def solution(d, budget):
    for i, amount in enumerate(sorted(d)):
        budget -= amount
        if budget < 0:
            return i
    return len(d)