def solution(x):
    i, z = 0, 0
    while x != '1' :
        i += 1
        z += x.count('0')
        x = bin(x.count('1'))[2:]
        
    return [i, z]