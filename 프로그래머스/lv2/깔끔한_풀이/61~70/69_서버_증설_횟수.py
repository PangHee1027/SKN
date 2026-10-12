from collections import deque

def solution(players, m, k):
    answer = 0
    # k시간 동안 유지되는 서버들의 증설 기록을 관리하는 큐
    server_queue = deque([0] * k, maxlen=k)
    current_servers = 0  # 현재 운영 중인 총 증설 서버 수

    for player in players:
        # 1. 만료 기간이 지난 서버를 총합에서 제외
        expired = server_queue.popleft()
        current_servers -= expired

        # 2. 현재 인원을 감당하기 위해 추가로 필요한 서버 수 계산
        # 감당 가능한 총 인원 = (기본 서버 1대 분량 + 현재 증설된 서버들) * m
        capacity = current_servers * m
        
        require = 0
        if player > capacity:
            # 부족한 인원을 m으로 나누어 필요한 서버 수 계산 (올림 처리)
            deficit = player - capacity
            require = (deficit + m - 1) // m  # 정수 연산을 이용한 올림

        # 3. 증설이 필요한 경우 처리
        answer += require
        current_servers += require
        server_queue.append(require)

    return answer