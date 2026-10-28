import sys
sys.setrecursionlimit(100000)

def solution(tickets):
    tickets.sort()  # 알파벳 순서가 앞서는 경로를 먼저 찾기 위해 정렬
    n = len(tickets)
    visited = [False] * n
    answer = []

    def dfs(current_airport, count):
        # 모든 티켓을 다 사용했다면 경로 완성
        if count == n:
            return True
        
        for i in range(n):
            if not visited[i] and tickets[i][0] == current_airport:
                visited[i] = True
                answer.append(tickets[i][1])
                
                # 다음 탐색이 성공하면 바로 종료
                if dfs(tickets[i][1], count + 1):
                    return True
                
                # 실패했다면 백트래킹 (원상복구)
                answer.pop()
                visited[i] = False
                
        return False

    # 항상 "ICN"에서 출발
    answer.append("ICN")
    dfs("ICN", 0)
    
    return answer