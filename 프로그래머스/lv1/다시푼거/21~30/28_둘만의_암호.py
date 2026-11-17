import string

def solution(s, skip, index):
    alpha = [x for x in string.ascii_lowercase if x not in skip]
    n = len(alpha)
    s2n = {j : i for i, j in enumerate(alpha)}
    n2s = {i : j for i, j in enumerate(alpha)}
    return ''.join(n2s[(s2n[x] + index) % n] for x in s)