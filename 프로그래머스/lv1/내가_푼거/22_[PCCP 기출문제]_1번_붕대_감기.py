def solution(bandage, health, attacks):
    attack_dic = dict(attacks)
    current_health = health
    start_time = 0
    for i in range(attacks[-1][0] + 1) :
        is_attacked = False
        if (attack_dic.get(i)) :
            current_health -= attack_dic.get(i)
            is_attacked = True
            start_time = 0
            if current_health <= 0 :
                return -1
        if not is_attacked :
            current_health += bandage[1]
            start_time += 1
            if start_time % bandage[0] == 0 :
                current_health += bandage[2]
        current_health = min(health, current_health)
        print(current_health)
    return current_health

# print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))