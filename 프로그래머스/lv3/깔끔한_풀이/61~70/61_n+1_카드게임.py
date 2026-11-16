def solution(coin, cards):
    n = len(cards)
    n_plus_one = n + 1
    initial = n // 3
    max_round = (n - initial) // 2 + 1
    
    my_deck = set(cards[:initial])
    candidate = set()

    idx = initial
    for iter in range(max_round):
        # 1. 매 라운드 시작 시 카드 2장을 후보군에 추가
        candidate.update(cards[idx : idx + 2])
        idx += 2
        
        found = False
        
        # 전략 1: 동전 0개 소모 (내 덱 안에서 페어 찾기)
        for card in list(my_deck):
            pair = n_plus_one - card
            if card in my_deck and pair in my_deck and card != pair:
                my_deck.remove(card)
                my_deck.remove(pair)
                found = True
                break
        if found:
            continue

        # 전략 2: 동전 1개 소모 (내 덱 카드 1장 + 후보군 카드 1장)
        if coin >= 1:
            for card in list(my_deck):
                pair = n_plus_one - card
                if pair in candidate:
                    my_deck.remove(card)
                    candidate.remove(pair)
                    coin -= 1
                    found = True
                    break
        if found:
            continue

        # 전략 3: 동전 2개 소모 (후보군 카드끼리 페어)
        if coin >= 2:
            for card in list(candidate):
                pair = n_plus_one - card
                if card in candidate and pair in candidate and card != pair:
                    candidate.remove(card)
                    candidate.remove(pair)
                    coin -= 2
                    found = True
                    break
        if found:
            continue
            
        # 페어를 찾지 못했다면 현재 라운드까지만 진행 가능
        return iter + 1

    return max_round