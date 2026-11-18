def solution(bandage, health, attacks):
    hp = health
    last_attack = 0
    
    for t, damage in attacks :
        if last_attack :
            duration = t - last_attack - 1
            heal = duration * bandage[1] + ((duration // bandage[0]) * bandage[2])
            hp = min(health, hp + heal)
        hp -= damage
        last_attack = t
        if hp <= 0 :
            return -1
        
    return hp