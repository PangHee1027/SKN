def get_gcb(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def solution(w,h):
    extent = w * h
    gcb = get_gcb(w, h)
    a, b = w // gcb, h // gcb
    diagonal = a + b - 1
    return extent - (diagonal * gcb)

print(solution(8, 12))