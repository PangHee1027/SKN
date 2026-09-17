# 함수 만들어서 한거 빼면 코드 자체는 크게 다를게 없음
# 다만 처음에 index()를 사용해서 해서 시간 복잡도가 너무 높아져서 디렉토리를 쓰는 쪽으로 변경했음
def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players