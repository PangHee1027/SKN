from itertools import combinations

def solution(friends, gifts) :
    friend_idx = {friend : i for i, friend in enumerate(friends)}
    n = len(friends)
    nxt_gift = [0] * n
    gift_matrix = [[0] * n for _ in range(n)]
    for gift in gifts :
        giver, reciever = gift.split()
        gift_matrix[friend_idx[giver]][friend_idx[reciever]] += 1
    
    for f1, f2 in combinations(range(n), 2) :
        if gift_matrix[f1][f2] > gift_matrix[f2][f1] :
            nxt_gift[f1] += 1
        elif gift_matrix[f1][f2] < gift_matrix[f2][f1] :
            nxt_gift[f2] += 1
        else :
            gift_point1 = sum(gift_matrix[f1]) - sum(gift_matrix[i][f1] for i in range(n))
            gift_point2 = sum(gift_matrix[f2]) - sum(gift_matrix[i][f2] for i in range(n))
            if gift_point1 > gift_point2 :
                nxt_gift[f1] += 1
            elif gift_point1 < gift_point2 :
                nxt_gift[f2] += 1
    return max(nxt_gift)