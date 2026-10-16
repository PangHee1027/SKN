def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1  # 우측으로 쭉 가는 기본 이동 횟수
    
    for i, char in enumerate(name):
        # 1. 상하 조작 횟수 (위로 가는 것과 아래로 돌아가는 것 중 최솟값)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 2. 좌우 이동 횟수 최솟값 갱신 (연속된 'A' 구간 활용)
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        # 세 가지 경우의 수 중 최솟값 선택:
        # ① 기본 (우측으로 쭉)
        # ② 우측으로 갔다가 좌측으로 꺾기: i * 2 + (n - next_i)
        # ③ 좌측으로 먼저 갔다가 우측으로 꺾기: (n - next_i) * 2 + i
        min_move = min(min_move, i * 2 + n - next_i, (n - next_i) * 2 + i)
        
    return answer + min_move