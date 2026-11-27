from math import factorial

def solution(n, k) :
    remain = list(range(1, n + 1))
    dividor = factorial(n - 1)
    nxt = n - 1
    answer = []
    k -= 1
    while len(remain) > 1 :
        div, k = divmod(k, dividor)
        answer.append(remain[div])
        remain.pop(div)
        dividor //= nxt
        nxt -= 1
        print(remain, div, k)
        
    return answer + remain