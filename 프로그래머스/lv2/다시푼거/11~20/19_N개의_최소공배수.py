from math import lcm

def solution(arr):
    n_lcm = 1
    for n in arr :
        n_lcm = lcm(n_lcm, n)

    return n_lcm