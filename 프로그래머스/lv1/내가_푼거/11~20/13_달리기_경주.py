def swap(player_dict, players, player) :
    index, pre_index = player_dict[player], player_dict[player] - 1
    players[index], players[pre_index] = players[pre_index], players[index]
    player_dict[player] -= 1
    player_dict[players[index]] += 1

def solution(players, callings):
    player_dict = {player: i for i, player in enumerate(players)}
    for i in callings :
        swap(player_dict, players, i)
    return players

# print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))