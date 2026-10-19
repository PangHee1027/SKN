from collections import Counter

def solution(points, routes):
    # 0-indexed로 변환된 포인트 딕셔너리
    p_dict = {i + 1: (p[0] - 1, p[1] - 1) for i, p in enumerate(points)}
    
    robot_paths = []
    
    # 1. 각 로봇별로 0초부터 끝까지 거치는 모든 좌표(시간 순서대로)를 미리 계산
    for route in routes:
        path = []
        # 시작 지점
        curr_r, curr_c = p_dict[route[0]]
        path.append((curr_r, curr_c))
        
        for target_idx in route[1:]:
            target_r, target_c = p_dict[target_idx]
            
            # r 좌표 먼저 이동
            while curr_r != target_r:
                if curr_r < target_r:
                    curr_r += 1
                else:
                    curr_r -= 1
                path.append((curr_r, curr_c))
            
            # c 좌표 이동
            while curr_c != target_c:
                if curr_c < target_c:
                    curr_c += 1
                else:
                    curr_c -= 1
                path.append((curr_r, curr_c))
                
        robot_paths.append(path)
        
    # 2. 가장 긴 경로의 시간(초) 구하기
    max_time = max(len(path) for path in robot_paths)
    
    total_crash = 0
    
    # 3. 시간대별(t초)로 로봇들의 위치를 확인하여 충돌 체크
    for t in range(max_time):
        positions = []
        for path in robot_paths:
            # 로봇이 이미 목적지에 도착해 센터를 벗어났다면 제외
            if t < len(path):
                positions.append(path[t])
                
        # 해당 초에 같은 좌표에 있는 로봇 수 계산
        counts = Counter(positions)
        for pos, count in counts.items():
            if count > 1:
                total_crash += 1
                
    return total_crash