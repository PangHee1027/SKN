def solution(n) : 
    bin_n = bin(n)[2:]
    count_1 = bin_n.count('1')
    while True :
        n += 1
        if bin(n).count('1') == count_1 :
            return n
    