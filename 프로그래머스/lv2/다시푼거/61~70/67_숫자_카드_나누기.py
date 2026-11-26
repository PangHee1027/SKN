from math import gcd

def solution(arrayA, arrayB):
    gcd_a = gcd(*arrayA)
    gcd_b = gcd(*arrayB)
    
    for x in arrayB :
        if not x % gcd_a :
            gcd_a = 0
            break
            
    for x in arrayA :
        if not x % gcd_b :
            gcd_b = 0
            break
            
    return max(gcd_a, gcd_b)