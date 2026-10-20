def solution(cards) :
    answer = 0
    groups = []
    len_cards = len(cards)

    iter = 0
    pass_iter = []

    while sum(len(x) for x in groups) < len_cards :
        while iter in pass_iter :
            iter += 1    
        if iter >= len_cards :
            break

        s = set()
        card = cards[iter]
        s.add(card)
        pass_iter.append(iter)
        next_iter = card - 1
        next_card = cards[next_iter]

        while next_card not in s :
            pass_iter.append(next_iter)
            s.add(next_card)

            next_iter = next_card - 1
            next_card = cards[next_iter]

        groups.append(s)
        
    groups.sort(key = lambda x : len(x))

    if len(groups) == 1 :
        return 0
            
    return len(groups[-1]) * len(groups[-2])

print(solution([8, 6, 3, 7, 2, 5, 1, 4])) # 12