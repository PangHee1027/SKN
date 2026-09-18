from collections import Counter


def solution(N, stages):
    stage_counts = Counter(stages)
    total_players = len(stages)  # 전체 도달 플레이어 수
    fail_rates = {}

    for stage in range(1, N + 1):
        if total_players > 0:
            count = stage_counts[stage]  # 해당 스테이지에 멈춰있는 인원
            fail_rates[stage] = count / total_players  # 실패율 = 멈춰있는 인원 / 도달한 인원
            total_players -= count  # 다음 스테이지 도달 인원은 현재 멈춘 인원을 뺀 값
        else:
            # 도달한 플레이어가 0명이면 실패율은 0
            fail_rates[stage] = 0

    # 실패율 내림차순(x[1] reverse), 실패율이 같으면 스테이지 번호 오름차순(x[0])
    return sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)