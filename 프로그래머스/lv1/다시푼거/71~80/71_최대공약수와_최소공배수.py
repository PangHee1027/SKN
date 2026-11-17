def get_gcb(a, b) :
    while b != 0 :
        a, b = b, a % b
    return a

def solution(n, m):
    gcb = get_gcb(n, m)
    return [gcb, n * m // gcb]