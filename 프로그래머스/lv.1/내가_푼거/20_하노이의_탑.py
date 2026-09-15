def hanoi(n, start, sub, reverse) :
    if n == 1 and not sub:
        return [start, 3]
    elif n == 1 and sub :
        return [start, 2 if start == 1 else 2]
    elif reverse and sub:
        return 

    

def solution(n):
    answer = []
    
    return answer

print(hanoi(3))