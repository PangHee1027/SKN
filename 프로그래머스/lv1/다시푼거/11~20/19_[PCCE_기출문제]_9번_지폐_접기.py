def solution(wallet, bill):
    wallet.sort()
    bill.sort()
    answer = 0
    
    while wallet[0] < bill[0] or wallet[1] < bill[1] :
        answer += 1
        bill[1] //= 2
        bill.sort()
        
    return answer