def solution(park, routes):
    h, w = len(park), len(park[0])
    
    # 1. 시작 위치(S) 찾기
    r, c = 0, 0
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                r, c = i, j
                break

    # 2. 방향별 (dy, dx) 정의
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    # 3. 명령 수행
    for route in routes:
        dir_op, step = route.split()
        step = int(step)
        dr, dc = direction[dir_op]

        nr, nc = r, c
        valid = True

        # 한 칸씩 이동하며 범위 및 장애물 검사
        for _ in range(step):
            nr += dr
            nc += dc

            # 공원을 벗어나거나 장애물을 만난 경우 이동 불가
            if not (0 <= nr < h and 0 <= nc < w) or park[nr][nc] == "X":
                valid = False
                break

        # 명령을 정상 수행한 경우에만 위치 업데이트
        if valid:
            r, c = nr, nc

    return [r, c]