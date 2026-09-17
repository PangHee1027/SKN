def solution(wallet, bill):
    answer = 0

    while max(wallet) < max(bill) or min(wallet) < min(bill) :
        bill.sort()
        bill[1] = bill[1] // 2
        answer += 1

    return answer

# print(solution([50, 50], [100, 241]))