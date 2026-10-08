from collections import deque


def solution(bridge_length, weight, truck_weights):
  # time: 현재 경과 시간 (초)
  time = 0

  # bridge: 다리 위를 지나고 있는 트럭의 정보를 담는 큐
  # 각 요소는 (트럭 무게, 해당 트럭이 다리를 완전히 건너 내리는 시각) 형태의 튜플
  bridge = deque()

  # current_weight: 현재 다리 위에 올라가 있는 트럭들의 총무게
  current_weight = 0

  # trucks: 다리를 건너기 위해 대기 중인 트럭들의 무게 큐
  trucks = deque(truck_weights)

  # 대기 중인 트럭이 남아있는 동안 반복 시뮬레이션 진행
  while trucks:
    # 1초 경과
    time += 1

    # 1. 다리의 가장 맨 앞 트럭(bridge[0])이 내릴 시각이 되었다면 하차 처리
    if bridge and bridge[0][1] == time:
      passed_weight, _ = bridge.popleft()  # 다리에서 트럭 이탈
      current_weight -= passed_weight  # 현재 다리 위 총무게 감소

    # 2. 다음 대기 트럭(trucks[0])이 다리에 올라올 수 있는지 무게 한도 확인
    if current_weight + trucks[0] <= weight:
      # 대기열에서 트럭을 꺼내 다리에 탑승
      truck = trucks.popleft()
      current_weight += truck  # 현재 다리 위 총무게 증가

      # (트럭 무게, 다리를 완전히 건너는 시각)을 다리 큐에 기록
      # time초에 다리에 올라갔으므로, bridge_length초 후인 (time + bridge_length)에 하차함
      bridge.append((truck, time + bridge_length))
    else:
      # 3. 무게 초과로 다음 트럭이 바로 진입할 수 없는 경우 (시간 점프 최적화)
      # 가장 먼저 내릴 트럭(bridge[0])이 탈출할 시각으로 시간을 한 번에 건너뜁니다.
      # 다음 루프 시작 시 time += 1 이 실행되므로, 목적 시각보다 1초 전(-1)으로 설정합니다.
      time = bridge[0][1] - 1

  # 모든 대기 트럭이 다리에 올라타고 루프가 종료되었을 때,
  # 다리의 맨 마지막 트럭(bridge[-1])이 다리를 완전히 건너는 시각을 최종 반환
  return bridge[-1][1]