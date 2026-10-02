def solution(dirs):
    # 1. 이동 방향 정의
    move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    visited = set()
    x, y = 0, 0  # 현재 위치

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy

        # 2. 맵 범위(-5 ~ 5)를 벗어나면 무시
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        # 3. 양방향 경로를 set에 추가 (중복은 set이 알아서 제거)
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))

        # 4. 위치 이동
        x, y = nx, ny

    # 양방향으로 저장했으므로 2로 나눈 값이 처음 걸어본 길의 길이
    return len(visited) // 2