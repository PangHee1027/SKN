def solution(wallet, bill):
    answer = 0
    wallet.sort()  # wallet을 미리 정렬 (wallet[0]: min, wallet[1]: max)

    while True:
        bill.sort()
        # 지폐의 작은 쪽이 지갑의 작은 쪽보다 작거나 같고, 
        # 지폐의 큰 쪽이 지갑의 큰 쪽보다 작거나 같으면 종료
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break

        bill[1] //= 2
        answer += 1

    return answer