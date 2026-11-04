from itertools import permutations

def solution(n, weak, dist):
    checkpoint = len(weak)
    
    # 1. 원형 외벽을 일자로 펴기 위해 길이를 2배로 늘림 (시계 방향 탐색을 연속적으로 처리하기 위함)
    extended_weak = weak + [x + n for x in weak]
    
    # 2. 투입할 친구의 수를 1명부터 시작해서 점차 늘려감 (최소값을 구해야 하므로 작은 수부터 탐색)
    for num_of_friends in range(1, len(dist) + 1):
        
        # 3. 친구들을 배치하는 모든 순서(순열)를 완전탐색
        for permutation in permutations(dist, num_of_friends):
            
            # 4. 각 취약 지점을 시작점(i)으로 설정하여 시뮬레이션 진행
            for i in range(checkpoint):
                idx = i  # 현재 점검 중인 취약 지점 인덱스
                
                # 5. 현재 순서의 친구들을 차례대로 투입
                for distance in permutation:
                    current_position = extended_weak[idx]
                    
                    # 현재 친구가 이동할 수 있는 거리(distance) 내에 있는 취약 지점들을 모두 방문 처리
                    while idx < i + checkpoint and extended_weak[idx + 1] - current_position <= distance:
                        idx += 1
                    
                    idx += 1  # 다음 친구가 출발할 취약 지점으로 이동
                    
                    # 시작점부터 시작해서 checkpoint만큼의 모든 취약 지점을 다 점검했다면 현재 친구 수 반환
                    if idx >= i + checkpoint:
                        return num_of_friends
                        
    # 모든 친구를 다 투입해도 모든 취약 지점을 점검할 수 없는 경우
    return -1   