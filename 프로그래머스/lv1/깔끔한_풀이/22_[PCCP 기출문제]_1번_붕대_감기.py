def solution(bandage, health, attacks):
    cast_time, recover_per_sec, bonus_recover = bandage
    current_health = health
    last_attack_time = 0  # 이전 공격 시간 (초기값 0초)

    for attack_time, damage in attacks:
        # 1. 이전 공격 이후부터 현재 공격 직전까지 연속 붕대 감기 가능 시간 계산
        time_gap = attack_time - last_attack_time - 1

        if time_gap > 0:
            # 기본 회복 + 연속 성공에 따른 추가 회복
            total_heal = (time_gap * recover_per_sec) + ((time_gap // cast_time) * bonus_recover)
            current_health = min(health, current_health + total_heal)

        # 2. 몬스터 공격 적용 및 연속 성공 초기화
        current_health -= damage
        if current_health <= 0:
            return -1

        last_attack_time = attack_time

    return current_health