import numpy as np

# 신호들의 전체 사이클의 최소공배수 계산
def lcm_calc(sig) :
    nums = []
    for i in sig :
        nums.append(i[0] + i[1] + i[2])
    return np.lcm.reduce(nums)

def solution(signals = 0):
    # 아무 것도 입력되지 않으면 -1 반환
    if not signals :
        return -1

    lcm = lcm_calc(signals)

    # 최소공배수까지 계산 (최소공배수 이후는 다시 반복일테니)
    for t in range(1, lcm + 1) :
        is_all_yellow = True

        # signals의 각 원소의 초록, 노랑, 빨강 신호를 추출
        for g, y, r in signals :
            # 전체 사이클을 계산
            cycle_length = g + y + r
            # 현재 시간이 사이클의 어디에 위치해 있는지 계산 ex) 현재 시간 = 8, 전체 사이클 = 5 -> 8 % 5 = 3 즉 사이클의 3번째 라는 것
            current = t % cycle_length

            # 현재가 초록이 꺼진시간(노랑이 켜진 시간)과 노랑이 꺼지기 전 시간 사이가 아니라면 사이클을 종료
            if not (g < current <= g + y) :
                is_all_yellow = False
                break

        if is_all_yellow :
            return t
        
    # 사이클을 종료하였는데 찾지 못했다면 모든 노란불이 켜지는 시간이 없으니 -1 반환
    return -1
