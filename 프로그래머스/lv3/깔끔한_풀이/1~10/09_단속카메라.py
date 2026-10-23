def solution(routes):
    # 차량의 진출 지점 기준 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_count = 0
    last_camera_pos = -float("inf")

    for start, end in routes:
        # 현재 차량의 진입 지점이 마지막 카메라 위치보다 뒤에 있다면 새로운 카메라 필요
        if start > last_camera_pos:
            camera_count += 1
            last_camera_pos = end  # 현재 차량의 진출 지점에 카메라 설치

    return camera_count