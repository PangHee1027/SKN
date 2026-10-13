def solution(places):
    answer = []
    
    def check_place(place):
        h, w = len(place), len(place[0])
        
        for r in range(h):
            for c in range(w):
                if place[r][c] != 'P':
                    continue
                
                # 현재 응시자(r, c)를 기준으로 맨해튼 거리 2 이하인 모든 칸 탐색
                for nr in range(h):
                    for nc in range(w):
                        dist = abs(r - nr) + abs(c - nc)
                        
                        # 거리가 1 또는 2인 위치에 다른 응시자('P')가 있는 경우
                        if 0 < dist <= 2 and place[nr][nc] == 'P':
                            # 1) 거리가 1이면 무조건 위반
                            if dist == 1:
                                return False
                            
                            # 2) 거리가 2인 경우, 사이에 파티션('X')이 있는지 확인
                            # 같은 행에 있는 경우 (가로 사이)
                            if r == nr:
                                if place[r][(c + nc) // 2] != 'X':
                                    return False
                            # 같은 열에 있는 경우 (세로 사이)
                            elif c == nc:
                                if place[(r + nr) // 2][c] != 'X':
                                    return False
                            # 대각선에 있는 경우 (코너 칸들에 파티션이 모두 있어야 함)
                            else:
                                if place[r][nc] != 'X' or place[nr][c] != 'X':
                                    return False
        return True

    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer